from ..animal import Animal

class Sheep(Animal):
    def __init__(self, loc, wrld):
        super().__init__("Sheep", 4, 4, 1, loc, wrld)
