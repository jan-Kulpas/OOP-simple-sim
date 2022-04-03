from ..animal import Animal

class Fox(Animal):
    def __init__(self, loc, wrld):
        super().__init__("Fox", 3, 7, 1, loc, wrld)
    def calc_move_flag(self, newloc):
        if not self.is_oob(newloc):
            target = self.home.map[newloc]
            if not target:
                self.home.log.append("{0} moves to tile ({1},{2})".format(
                self.name, *newloc))
                return True
            elif self.strength >= target.strength:
                return self.collide(target)
            else:
                self.home.log.append("{0} decided to avoid tile ({1},{2})".format(
                self.name, *newloc))
                return False
        return False
