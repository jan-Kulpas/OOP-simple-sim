from .entity import Entity
import random

class Plant(Entity):
    def __init__(self, n, str, loc, wrld):
        super().__init__(n, str, 0, 0, loc, wrld)

    def move(self):
        if self.child:
            self.child = False
            return
        if random.random() <= 0.15:
            self.multiply()

    def collide(self, other):
        return False
