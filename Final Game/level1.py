#Sherry Zhang
#11/18/21

#Level 1 of Final Game

import os, pygame
from pygame.locals import *

os.system('clear')
pygame.init()

WIDTH, HEIGHT = 700, 700

window = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.image.load("Final Game/Images/background.png")
pink_sprite_l = [pygame.image.load("Final Game/Images/sprite_pink/pinkL1.png"), 
                pygame.image.load("Final Game/Images/sprite_pink/pinkL2.png"), 
                pygame.image.load("Final Game/Images/sprite_pink/pinkL3.png")]
pink_sprite_r = [pygame.image.load("Final Game/Images/sprite_pink/pinkR1.png"), 
                pygame.image.load("Final Game/Images/sprite_pink/pinkR2.png"), 
                pygame.image.load("Final Game/Images/sprite_pink/pinkR3.png")]
pink_sprite_u = [pygame.image.load("Final Game/Images/sprite_pink/pinkU1.png"), 
                pygame.image.load("Final Game/Images/sprite_pink/pinkU2.png"), 
                pygame.image.load("Final Game/Images/sprite_pink/pinkU3.png")]

run = True
#Variables for sprite position
sprite_pos_x = 0
sprite_pos_y = 0

image = pink_sprite_l[0]

sprite_direction = "right"

#sprite_num - used to calculate which sprite to use out of list of 3
sprite_num = 0

while run:
    window.blit(background, (0,0))
    # print(pygame.mouse.get_pos())
    keyPressed = pygame.key.get_pressed()

    if (sprite_num // 15) == len(pink_sprite_l):
        sprite_num = 0

    #Choose sprite direction and then choose image
    if sprite_direction == 'left':
        image = pink_sprite_l[sprite_num // 15]

    elif sprite_direction == 'right':
        image = pink_sprite_r[sprite_num // 15]

    elif sprite_direction == 'up':
        image = pink_sprite_u[sprite_num // 15]

    sprite = window.blit(image, (sprite_pos_x, sprite_pos_y))
    print(sprite_pos_x, sprite_pos_y)


    if 0 <= sprite_pos_x < WIDTH - image.get_width() and 0 <= sprite_pos_y < HEIGHT - image.get_height():   
        if keyPressed[K_LEFT]:
            sprite_pos_x -= 5
            sprite_num += 1
            sprite_direction = 'left'
        
        elif keyPressed[K_RIGHT]:
            sprite_pos_x += 5
            sprite_num += 1
            sprite_direction = 'right'
        
        elif keyPressed[K_UP]:
            sprite_pos_y -= 5
            sprite_num += 1
            sprite_direction = 'up'
        
        elif keyPressed[K_DOWN]:
            sprite_num += 1
            sprite_pos_y += 5
    
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
