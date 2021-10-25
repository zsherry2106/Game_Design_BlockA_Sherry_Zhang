#Sherry Zhang
#10/25/21

#Pygame fonts

import pygame as py, os
os.system('clear')

py.init()

WIDTH, HEIGHT = 800
window = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_captino("Setting Window")

#pygame font has 4 parameters: name, size, bold, and italic
TITLE_FONT = py.font.SysFont("Arial", 12, bold = False, italic = False)
