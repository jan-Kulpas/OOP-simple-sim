from ..animal import Animal
import random

class Turtle(Animal):
    def __init__(self, loc, wrld):
        super().__init__("Turtle", 2, 1, 1, loc, wrld)
    def has_blocked(self, other):
        if other.strength < 5:
            self.home.log.append("{0} blocks attack from {1} at ({2},{3})".format(
            self.name, other.name, *self.location))
            return True
        return False
    def move(self):
        if not random.randrange(4):
            super().move()
