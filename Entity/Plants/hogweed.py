from ..plant import Plant
import numpy as np

class Hogweed(Plant):
    def __init__(self, loc, wrld):
        super().__init__("Hogweed", 10, loc, wrld)

    def move(self):
        if self.child:
            self.child = False
            return

        modifiers = [(1,0),(0,1),(-1,0),(0,-1)]

        for mod in modifiers:
            newloc = tuple(np.add(self.location, mod))
            if not self.is_oob(newloc):
                target = self.home.map[newloc]
                if target and target.initiative > 0 and target.strength <= self.strength:
                    self.home.log.append("{0} gets burnt by Hogweed at ({1},{2})".format(
                    target.name, *target.location))
                    self.home.remove_entity(target)

        super().move()
