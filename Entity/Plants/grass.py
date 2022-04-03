from ..plant import Plant

class Grass(Plant):
    def __init__(self, loc, wrld):
        super().__init__("Grass", 0, loc, wrld)
