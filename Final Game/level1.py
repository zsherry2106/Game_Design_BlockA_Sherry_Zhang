#Sherry Zhang
#11/18/21

#Level 1 of Final Game

import os, pygame
from pygame.locals import *

os.system('clear')
pygame.init()

WIDTH, HEIGHT = 700, 700

window = pygame.display.set_mode((WIDTH, HEIGHT))

background_tile = pygame.image.load("Final Game/Images/background_tile.png")
background_grass = pygame.image.load("Final Game/Images/background_grass.png")

run = True

while run:
    window.blit(background_grass, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    
    pygame.display.flip()
