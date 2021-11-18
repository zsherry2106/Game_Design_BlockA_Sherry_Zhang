#Sherry Zhang
#10/15/21

#Pygame notes/test page
#Learn display, 
# Opening windows, 
# Changing window size, 
# Basic game loop

import pygame, os, random
from pygame.locals import *
pygame.init()
os.system('clear')


colors = {'black':(0,0,0), 
          'red':(255,0,0), 
          'green':(0,255,0), 
          'blue':(0,0,255), 
          'white':(255,255,255), 
          'purple':(169,77,255),
          'orange':(255,160,77)
          }

width = 500
height = 500

window = pygame.display.set_mode((width, height))

color = 'white'
color = colors.get(color)

background = pygame.image.load('Pygame/Circle Square Game/Images/background.jpg')
sprites = pygame.image.load('Pygame/Circle Square Game/Images/walking_sprite.png')

window.fill(color)
pygame.display.set_caption("Game Window")
running = True
direction = 'right'

walk_x = 0
walk_y = 270
sprite_width = 80
sprite_height = 110

image_count = 0
right_image_list = [[25, 10, 80, 110], [116, 12, 100, 123], [220, 10, 115, 102]]
left_image_list = [[0,151, 93, 104], [100,153,115,102], [215, 155, 95, 126]]

x_pos_background = 0


jumping = False
jumpCount = 10
walk = True

speed = 5

while running:
    pygame.time.delay(10)
    window.blit(background, (x_pos_background,0))
    sprite_num = image_count // 15

    if sprite_num == len(right_image_list) or sprite_num == len(left_image_list):
        sprite_num = 0
        image_count = 0
    
    if direction == 'right':
        sprite_x = right_image_list[sprite_num][0]
        sprite_y = right_image_list[sprite_num][1]
        sprite_width = right_image_list[sprite_num][2]
        sprite_height = right_image_list[sprite_num][3]
    else:
        sprite_x = left_image_list[sprite_num][0]
        sprite_y = left_image_list[sprite_num][1]
        sprite_width = left_image_list[sprite_num][2]
        sprite_height = left_image_list[sprite_num][3]


    walking_1 = window.blit(sprites, (walk_x, walk_y), (sprite_x, sprite_y, sprite_width, sprite_height))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    keyPressed = pygame.key.get_pressed()

    if keyPressed[pygame.K_RIGHT]:
        direction = 'right'
        image_count += 1
        x_pos_background -= 1

    elif keyPressed[pygame.K_LEFT]:
        direction = 'left'
        image_count += 1
        x_pos_background += 1

    if not jumping:
        if keyPressed[pygame.K_SPACE]:
            jumping = True

    elif jumping:
        if jumpCount >= -10:
            walk_y -= jumpCount*abs(jumpCount)*0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            jumping = False

    if walk_x < 0:
        walk_x = 0
    elif walk_x > width - sprite_width:
        walk_x = width - sprite_width

    if walk_y < 0:
        walk_y = 0
    elif walk_y > height - sprite_height:
        walk_y = height - sprite_height

    pygame.display.flip()
