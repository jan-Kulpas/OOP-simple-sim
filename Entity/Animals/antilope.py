from ..animal import Animal
import random
import numpy as np

class Antilope(Animal):
    def __init__(self, loc, wrld):
        super().__init__("Antilope", 4, 4, 2, loc, wrld)
    def has_ran_away(self, other):
        if not random.randrange(2):
            return False
        else:
            modifiers = [(1,0),(0,1),(-1,0),(0,-1)]
            move_flag = False

            while(len(modifiers)):
                mod = random.choice(modifiers)
                newloc = tuple(np.add(self.location, mod))
                if not self.is_oob(newloc):
                    if not self.home.map[newloc]:
                        move_flag = True
                        break
                modifiers.remove(mod)
            if move_flag:
                self.home.log.append("{0} runs away to ({1},{2})".format(
                self.name, *newloc))
                loc = self.location
                self.home.map[loc], self.home.map[newloc] = self.home.map[newloc], self.home.map[loc]
                self.location = newloc
                return True
        return False
