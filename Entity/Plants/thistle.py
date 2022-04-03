from ..plant import Plant

class Thistle(Plant):
    def __init__(self, loc, wrld):
        super().__init__("Thistle", 0, loc, wrld)

    def move(self):
        if self.child:
            self.child = False
            return
        for x in range(3):
            super().move()
