import pygame
import os, sys
import random
from world import World
from Entity.Animals.wolf import Wolf
from Entity.Animals.sheep import Sheep
from Entity.Animals.fox import Fox
from Entity.Animals.turtle import Turtle
from Entity.Animals.antilope import Antilope
from Entity.Animals.human import Human
from Entity.Animals.cybersheep import Cybersheep
from Entity.Plants.grass import Grass
from Entity.Plants.thistle import Thistle
from Entity.Plants.guarana import Guarana
from Entity.Plants.wolfberry import Wolfberry
from Entity.Plants.hogweed import Hogweed

pygame.font.init()

mainClock = pygame.time.Clock()

WIDTH, HEIGHT = 960, 540
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Krzysztof Kulpiński 184368")

FPS = 60

WHITE = "#ffffff"
BLACK = "#000000"
GREY = "#c0c0c0"
L_GREEN = "#b4ffb4"
M_GREEN = "#82cd82"
D_GREEN = "#509b50"
YELLOW = "#ffee75"

BLANK_TEX = pygame.image.load(os.path.join('Assets','blonk.png'))
SHEEP_TEX = pygame.image.load(os.path.join('Assets','shep.png'))
WOLF_TEX = pygame.image.load(os.path.join('Assets','welf.png'))
FOX_TEX = pygame.image.load(os.path.join('Assets','fax.png'))
TURTLE_TEX = pygame.image.load(os.path.join('Assets','turt.png'))
ANTILOPE_TEX = pygame.image.load(os.path.join('Assets','antlop.png'))
HUMAN_TEX = pygame.image.load(os.path.join('Assets','haman.png'))
CYBERSHEEP_TEX = pygame.image.load(os.path.join('Assets','cybershep.png'))
GRASS_TEX = pygame.image.load(os.path.join('Assets','gres.png'))
THISTLE_TEX = pygame.image.load(os.path.join('Assets','thisml.png'))
GUARANA_TEX = pygame.image.load(os.path.join('Assets','guran.png'))
WOLFBERRY_TEX = pygame.image.load(os.path.join('Assets','welfber.png'))
HOGWEED_TEX = pygame.image.load(os.path.join('Assets','hegwed.png'))

SEL_SIZE = 20

TEX_DICT = {"Blank": BLANK_TEX, "Sheep": SHEEP_TEX, "Wolf": WOLF_TEX,
            "Fox": FOX_TEX, "Turtle": TURTLE_TEX, "Antilope": ANTILOPE_TEX,
            "Human": HUMAN_TEX, "Cybersheep": CYBERSHEEP_TEX, "Grass": GRASS_TEX,
            "Thistle": THISTLE_TEX, "Guarana": GUARANA_TEX, "Wolfberry": WOLFBERRY_TEX,
            "Hogweed": HOGWEED_TEX}
SEL_DICT = SCALED_TEX_DICT = {k: pygame.transform.scale(v, (SEL_SIZE, SEL_SIZE)) for k, v in TEX_DICT.items()}

font = pygame.font.SysFont("urwgothic", 36)
font_s = pygame.font.SysFont("urwgothic", 14)
font_es = pygame.font.SysFont("urwgothic", 10)

CLASS = {"Sheep": Sheep, "Wolf": Wolf, "Fox": Fox, "Turtle": Turtle,
        "Antilope": Antilope, "Human": Human, "Cybersheep": Cybersheep, "Grass": Grass, "Thistle": Thistle,
        "Guarana": Guarana, "Wolfberry": Wolfberry, "Hogweed": Hogweed}

WORLD_W = 0
WORLD_H = 0

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def menuDraw(selected):
    WINDOW.fill(L_GREEN)
    draw_text('New Game', font, GREY if selected == 0 else BLACK, WINDOW, 20, 20)
    draw_text('Load Game', font, GREY if selected == 1 else BLACK, WINDOW, 20, 80)
    draw_text('Quit', font, GREY if selected == 2 else BLACK, WINDOW, 20, 140)
    pygame.display.update()

def main():
    gameloop = True
    selected = 0
    while gameloop:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_DOWN and selected < 2:
                    selected += 1
                if event.key == pygame.K_UP and selected > 0:
                    selected -= 1
                if event.key in (pygame.K_SPACE, pygame.K_RETURN):
                    gameloop = False
                    [menuNew, menuLoad, gameQuit][selected]()

        menuDraw(selected)
        mainClock.tick(60)

    pygame.quit()

def menuNewDraw(text, selected, errtext):
    WINDOW.fill(D_GREEN)
    draw_text('Map width: '+text[0], font, GREY if selected == 0 else BLACK, WINDOW, 20, 20)
    draw_text('Map height: '+text[1], font, GREY if selected == 1 else BLACK, WINDOW, 20, 80)
    draw_text(errtext, font, BLACK, WINDOW, 20, 140)
    pygame.display.update()

def menuNew(errtext = ""):
    gameloop = True
    selected = 0
    text = ["",""]

    while gameloop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key in (pygame.K_SPACE, pygame.K_RETURN) and text[selected]:
                    if selected != 1:
                        selected += 1
                    else:
                        gameloop = False
                elif event.key == pygame.K_BACKSPACE:
                    text[selected] = text[selected][:-1]
                elif event.unicode.isdigit():
                    text[selected] += event.unicode


        menuNewDraw(text, selected, errtext)
        mainClock.tick(60)

    WORLD_W, WORLD_H = [int(x) for x in text]
    world = World(WORLD_W, WORLD_H)

    for key, item in CLASS.items():
        for i in range(2):
            r_loc = world.map.random_loc()
            if r_loc and (item != Human or i == 0):
                item(r_loc, world)

    game(world)

def menuLoad():
    f = open("gamedata.txt", "r")
    line = f.readline()
    world = World(*[int(x) for x in line.split()])
    for i in range(len(world.map)):
        line = f.readline()[:-1]
        if line:
            CLASS[line](i, world)
    f.close()
    game(world)

def gameQuit():
    pass

def gameDrawSel(selected):
    sel_x = (WIDTH//2-(len(SEL_DICT)-1)*SEL_SIZE)//2
    pygame.draw.rect(WINDOW, YELLOW, (sel_x + SEL_SIZE*selected, HEIGHT-20-SEL_SIZE, SEL_SIZE, SEL_SIZE))
    for i, t in enumerate(list(SEL_DICT.values())[1:]):
        x = sel_x + SEL_SIZE*i
        WINDOW.blit(t, (x, HEIGHT-20-SEL_SIZE))

def gameDraw(world, MAP_X, MAP_Y, DICT, TEX_SIZE, selected):
    WINDOW.fill(M_GREEN)
    for i, e in enumerate(world.map):
        tex = DICT[e.name] if e else DICT["Blank"]
        x = MAP_X + TEX_SIZE*(i%world.map.width)
        y = MAP_Y + TEX_SIZE*(i//world.map.width)
        WINDOW.blit(tex, (x, y))
    draw_text('Log: ', font_s, BLACK, WINDOW, 500, 20)
    cond = len(world.log)*20 - 40 < HEIGHT
    fo = font_s if cond else font_es
    mod = 20 if cond else 15
    for i, line in enumerate(world.log):
        ty = 40 + i*mod
        tx = 500
        draw_text(line, fo, BLACK, WINDOW, tx, ty)

    gameDrawSel(selected)
    pygame.display.update()

def game(world):
    def map_oob(mx, my):
        return mx < MAP_X or my < MAP_Y or mx > MAP_X+TEX_SIZE*world.map.width or my > MAP_Y+TEX_SIZE*world.map.height
    def sel_oob(mx, my):
        sel_x = (WIDTH//2-(len(SEL_DICT)-1)*SEL_SIZE)//2
        return mx < sel_x  or my < 500 or mx > sel_x + SEL_SIZE*(len(SEL_DICT)-1) or my > 500+SEL_SIZE
    def set_sel(mx):
        sel_x = (WIDTH//2-(len(SEL_DICT)-1)*SEL_SIZE)//2
        return (mx-sel_x)//SEL_SIZE

    TEX_SIZE = 120

    while True:
        MAP_X = (WIDTH//2 - TEX_SIZE*world.map.width)//2
        MAP_Y = ((HEIGHT-40-SEL_SIZE) - TEX_SIZE*world.map.height)//2
        if MAP_X < 10 or MAP_Y < 10:
            if TEX_SIZE > 20:
                TEX_SIZE -= 20
            else:
                menuNew("Map size too large.")
        else:
            break

    SCALED_TEX_DICT = {k: pygame.transform.scale(v, (TEX_SIZE, TEX_SIZE)) for k, v in TEX_DICT.items()}
    H_DIR = {pygame.K_UP: "up", pygame.K_LEFT: "left", pygame.K_RIGHT: "right", pygame.K_DOWN: "down", pygame.K_SPACE: "skip", pygame.K_z: "power"}

    selected = 0

    gameloop = True
    while gameloop:
        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save(world)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    save(world)
                if event.key in H_DIR.keys():
                    world.h_dir = H_DIR[event.key]
                    world.perform_turn()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not map_oob(mx, my):
                    newloc = ((mx-MAP_X)//TEX_SIZE, (my-MAP_Y)//TEX_SIZE)
                    if world.map[newloc]:
                        world.remove_entity(world.map[newloc])
                    list(CLASS.values())[selected](newloc, world)
                elif not sel_oob(mx, my):
                    selected = set_sel(mx)


        gameDraw(world, MAP_X, MAP_Y, SCALED_TEX_DICT, TEX_SIZE, selected)

def save(world):
    with open("gamedata.txt", "w+") as f:
        line = "{0} {1}".format(world.map.width, world.map.height)+os.linesep
        f.write(line)
        for e in world.map:
            line = e.name+os.linesep if e else os.linesep
            f.write(line)
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
