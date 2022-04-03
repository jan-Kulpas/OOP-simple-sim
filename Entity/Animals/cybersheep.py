from ..animal import Animal
import numpy as np

class Cybersheep(Animal):
    def __init__(self, loc, wrld):
        super().__init__("Cybersheep", 11, 4, 1, loc, wrld)

    def calc_dist(self, e_loc):
        return sum(np.absolute(np.subtract(self.location, e_loc)))

    def move(self):
        if(self.child):
            self.child = False
            return

        list = [(e.location, self.calc_dist(e.location)) for e in self.home.map
                if e and e.name == "Hogweed"]
        if not list:
            super().move()
            return
        closest, dist = min(list, key=lambda item: item[1])
        dir = np.subtract(self.location, closest)
        dir = (0, -dir[1]) if np.absolute(dir)[1]>np.absolute(dir)[0] else (-dir[0], 0)
        mod = tuple(np.sign(dir))

        mod = np.multiply(mod, self.speed)
        loc = self.location

        newloc = tuple(np.add(self.location, mod))

        move_flag = self.calc_move_flag(newloc)

        if move_flag:
            self.home.map[loc], self.home.map[newloc] = self.home.map[newloc], self.home.map[loc]
            self.location = newloc
