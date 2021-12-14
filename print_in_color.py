# code by Miguel Secillano:
#   github: secillanoma
#   youtube: FortuneEight / Miguel Secillano

"""
    This is a module for printing in color.
"""

import random as rn
from sty import fg, bg


def fg_random():
    return fg(rn.randint(0, 255), rn.randint(0, 255), rn.randint(0, 255))


def bg_random():
    return bg(rn.randint(0, 255), rn.randint(0, 255), rn.randint(0, 255))


def fg_shade(color):
    if color == "red":
        return fg(rn.randint(240, 255), rn.randint(64, 192), rn.randint(64, 192))
    if color == "green":
        return fg(rn.randint(64, 192), rn.randint(240, 255), rn.randint(64, 192))
    if color == "blue":
        return fg(rn.randint(64, 128), rn.randint(64, 192), rn.randint(240, 255))


def fg_print_rnd_char_clrs(string):
    for char in string:
        print(
            fg(rn.randint(64, 220), rn.randint(64, 220), rn.randint(64, 220)) + char,
            end="",
        )
    print()


clr_fg_red = fg(255, 0, 0)
clr_fg_green = fg(0, 255, 0)
clr_fg_blue = fg(0, 0, 255)
clr_fg_white = fg(255, 255, 255)
clr_fg_black = fg(0, 0, 0)
clr_fg_cyan = fg(0, 255, 255)
clr_fg_yellow = fg(255, 255, 0)
clr_fg_magenta = fg(255, 0, 255)

clr_fg_reset = fg.rs

clr_bg_red = bg(255, 0, 0)
clr_bg_green = bg(0, 255, 0)
clr_bg_blue = bg(0, 0, 255)
clr_bg_white = bg(255, 255, 255)
clr_bg_black = bg(0, 0, 0)
clr_bg_cyan = bg(0, 255, 255)
clr_bg_yellow = bg(255, 255, 0)
clr_bg_magenta = bg(255, 0, 255)

clr_bg_reset = bg.rs
