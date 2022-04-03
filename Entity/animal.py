from .entity import Entity
import numpy as np
import random

class Animal(Entity):
    def __init__(self, n, str, init, spd, loc, wrld):
        super().__init__(n, str, init, spd, loc, wrld)

    def calc_move_flag(self, newloc):
        if not self.is_oob(newloc):
            target = self.home.map[newloc]

            if not target:
                self.home.log.append("{0} moves to tile ({1},{2})".format(
                self.name, *newloc))
                return True
            else:
                return self.collide(target)
        return False

    def move(self):
        if(self.child):
            self.child = False
            return

        modifiers = [(1,0),(0,1),(-1,0),(0,-1)]
        mod = random.choice(modifiers)
        mod = np.multiply(mod, self.speed)
        loc = self.location

        newloc = tuple(np.add(self.location, mod))

        move_flag = self.calc_move_flag(newloc)

        if move_flag:
            self.home.map[loc], self.home.map[newloc] = self.home.map[newloc], self.home.map[loc]
            self.location = newloc

    def collide(self, other):
        o_n = other.name
        o_l = other.location
        if self.name == o_n:
            if not other.child:
                self.multiply()
            return False
        else:
            if other.has_ran_away(self):
                self.home.log.append("{0} tried to fight with {1} at tile ({2},{3}) but it ran away!".format(self.name, o_n, *o_l))
                return True
            else:
                if self.strength >= other.strength:
                    if(other.has_blocked(self)):
                        return False
                    else:
                        self.home.log.append("{0} wins a fight with {1} at tile ({2},{3})".format(self.name, o_n, *o_l))
                        self.home.remove_entity(other)
                        return True
                else:
                    self.home.log.append("{0} dies in a fight with {1} at tile ({2},{3})".format(self.name, o_n, *o_l))
                    self.home.remove_entity(self)
                    return False
        return False
