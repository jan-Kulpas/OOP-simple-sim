import random
from Entity.entity import Entity

class World:
    class Map:
        def __init__(self, w, h):
            self._data = [None for x in range(0, w*h)]
            self.width = w
            self.height = h

        def __getitem__(self, item):
            if type(item) == tuple:
                return self._data[self.index(item)]
            return self._data[item]

        def __setitem__(self, item, value):
            if type(item) == tuple:
                self._data[self.index(item)] = value
            else:
                self._data[item] = value

        def __len__(self):
            return self.width*self.height

        def random_loc(self):
            for i in range(10):
                x = random.randrange(self.width)
                y = random.randrange(self.height)
                if not self[(x,y)]:
                    return (x,y)
            return None

        def is_oob(self, loc):
            x, y = loc
            return (x < 0) or (x >= self.width) or (y < 0) or (y >= self.height)

        def index(self, tup):
            return tup[1] * self.width + tup[0]

    def __init__(self, w, h):
        self.map = self.Map(w,h)
        self.entities = []
        self.log = []
        self.h_dir = ""

    def add_entity(self, e):
        idx = len(self.entities)
        for i in range(0, len(self.entities)):
            if self.entities[i].initiative < e.initiative:
                idx = i
                break
        self.entities.insert(idx, e)
        self.map[e.location] = e

    def remove_entity(self, e):
        e.alive = False
        self.map[e.location] = None

    def draw_console(self):
        print("╔", end = '')
        for i in range(self.map.width*2-1):
            print("═", end = '')
        print("╗\n║", end = '')

        for i in range(self.map.width*self.map.height):
            if self.map[i]:
                print(self.map[i].name[:1], end = '')
            else:
                print(".", end = '')
            if (i+1)%self.map.width == 0:
                print("║")
                if i < (self.map.height-1)*self.map.width:
                    print("║", end = '')
            else:
                print(" ", end = '')

        print("╚", end = '')
        for i in range(self.map.width*2-1):
            print("═", end = '')
        print("╝\n", end = '')

    def perform_turn(self):
        self.log = []
        for e in self.entities:
            if e.alive:
                e.move()

        entities = [e for e in self.entities if e.alive]

    def print_map(self):
        print([x for x in self.map])
