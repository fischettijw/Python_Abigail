from sty import fg, bg

clr_red = fg(255, 0, 0)
clr_green = fg(0, 255, 0)
clr_blue = fg(0, 0, 255)
clr_magenta = fg(255, 0, 255)
clr_yellow = fg(255, 255, 0)
clr_cyan = fg(0, 255, 255)

clr_black = fg(0, 0, 0)
clr_white = fg(255, 255, 255)

clr_light_coral = fg(240, 128, 128)

import random
from random import randint as rnd


def fgRandom():
    return fg(rnd(0, 255), rnd(0, 255), rnd(0, 255))


def bgRandom():
    return bg(rnd(0, 255), rnd(0, 255), rnd(0, 255))
