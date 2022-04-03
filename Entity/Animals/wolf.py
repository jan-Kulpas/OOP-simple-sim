from ..animal import Animal

class Wolf(Animal):
    def __init__(self, loc, wrld):
        super().__init__("Wolf", 9, 5, 1, loc, wrld)
