import random
import numpy as np

class Entity:
    def __init__(self, n, str, init, spd, loc, wrld):
        self.name = n

        self.strength = str
        self.initiative = init
        self.speed = spd
        if type(loc) == tuple:
            self.location = loc
        else:
            w = wrld.map.width
            self.location = (loc%w, loc//w)
        self.home = wrld

        self.alive = True
        self.child = True

        self.home.add_entity(self)

    def is_oob(self, loc):
        return self.home.map.is_oob(loc)

    def has_blocked(self, other):
        return False

    def has_ran_away(self, other):
        return False

    def multiply(self):
        modifiers = [(1,0),(0,1),(-1,0),(0,-1)]

        while(len(modifiers)):
            mod = random.choice(modifiers)
            newloc = tuple(np.add(self.location, mod))
            if not self.is_oob(newloc):
                if not self.home.map[newloc]:
                    self.new_instance(newloc)
                    self.home.log.append("A new {0} is born at ({1},{2})".format(self.name, *newloc))
                    break
            modifiers.remove(mod)
        return

    def new_instance(self, loc):
        return type(self)(loc, self.home)

    def move(self):
        raise NotImplementedError()

    def collide(self, other):
        raise NotImplementedError()

    def draw():
        self.home.map[loc] = (self.name[:1], self)

    def __str__(self):
        return "A {0}.".format(self.name)

    def __repr__(self):
        return "<{0}:{1},{2},{3},[{4},{5}],A:{6};C:{7}>".format(
        self.name, self.strength, self.initiative, self.speed, *self.location, self.alive, self.child
        )
