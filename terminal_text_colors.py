# https://www.youtube.com/watch?v=aftw0WX4oCc
# https://pypi.org/project/sty/
# https://likegeeks.com/python-colors/
# https://www.youtube.com/watch?v=Scz-7S74wzY

import os

os.system("cls")

import random
from sty import fg, bg

clr_red = (255, 0, 0)
clr_green = (0, 255, 0)
clr_blue = (0, 0, 255)
clr_magenta = (255, 0, 255)
clr_yellow = (255, 255, 0)
clr_cursor = (200, 200, 200)


def clr_random():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )


def txt_clr(clr):
    print(fg(*clr), end="")


print("Cursor")
txt_clr(clr_cursor)
print("Cursor", "\n")


for clr in range(0, 20):
    txt_clr(clr_random())
    print("Hello World!")
print()
print("GOODBYE")
print()

txt_clr((255, 0, 255))
print("RGB manually defined (Magenta)", "\n")


print(bg.yellow, "this is a test", bg.black)


txt_clr(clr_red)
print("RED")
txt_clr(clr_green)  # green
print("GREEN")
txt_clr(clr_blue)
print("BLUE")
txt_clr(clr_cursor)
print("Cursor")
txt_clr((255, 255, 255))
print("Cursor")
txt_clr(clr_cursor)
print("Cursor")
