from ..animal import Animal
import numpy as np

class Human(Animal):
    def __init__(self, loc, wrld):
        super().__init__("Human", 5, 4, 1, loc, wrld)
        self.timer = 0

    def has_blocked(self, other):
        if self.timer <= 0:
            return False
        else:
            other.move()
            return True

    def move(self):
        if self.timer > -5:
            self.timer -= 1

        if self.home.h_dir == "power":
            self.ability()

        mod = {"up": (0,-1), "left": (-1,0), "right": (1,0),
                "down": (0,1), "power": (0,0), "skip": (0,0)}
        newloc = tuple(np.add(self.location, mod[self.home.h_dir]))

        move_flag = self.calc_move_flag(newloc)

        if move_flag:
            loc = self.location
            self.home.map[loc], self.home.map[newloc] = self.home.map[newloc], self.home.map[loc]
            self.location = newloc

    def ability(self):
        if self.timer == -5:
            self.timer = 5;
        return
