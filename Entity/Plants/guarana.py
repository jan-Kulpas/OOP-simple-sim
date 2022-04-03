from ..plant import Plant

class Guarana(Plant):
    def __init__(self, loc, wrld):
        super().__init__("Guarana", 0, loc, wrld)

    def has_blocked(self, other):
        other.strength += 3
        self.home.log.append("{0} strength increases by 3 at ({1},{2})".format(
        other.name, *self.location))
        return False
