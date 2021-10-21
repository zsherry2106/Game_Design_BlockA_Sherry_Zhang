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

# image = pygame.image.load("image.png")

# while 1:
#     height = input("Height from 100 - 1000: ")
#     width = input("Width from 100 - 1000: ")

#     if height.isdigit() and width.isdigit() and 100<=int(height)<=1000 and 100<=int(width)<=1000:
#         height = int(height)
#         width = int(width)
#         break
#     else:
#         print("Please enter numbers between 100 and 1000")

width = 500
height = 500

window = pygame.display.set_mode((width, height))

# color = input("Enter a color, red, green, blue, white, or black: ")
# color = colors.get(color)
color = random.choice(list(colors.keys()))
color = colors.get(color)

window.fill(color)
pygame.display.set_caption("Game Window")
running = True
rect_y = height/2
rect_x = width/2
wbox = 30
hbox = 30
radius = wbox/2
speed = 5
rect = pygame.Rect(width/2, height/2, wbox, hbox)
# circle = pygame.circle(width/4, height/4, radius)

while running:
    pygame.time.delay(10)
    window.fill(color)
    left_pressed, middle_pressed, right_pressed = pygame.mouse.get_pressed()
    # mouse = pygame.mouse.get_pos()
    # print(mouse
    pygame.draw.rect(window, colors.get('blue'), rect)
    # pygame.draw.circle(window, colors.get('blue'), (width/4, height/4), radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keyPressed = pygame.key.get_pressed()
    if keyPressed[pygame.K_UP]:
        rect_y -= speed
    if keyPressed[pygame.K_DOWN]:
        rect_y += speed
    if keyPressed[pygame.K_RIGHT]:
        rect_x += speed
    if keyPressed[pygame.K_LEFT]:
        rect_x -= speed
    
    # print(rect_y)

    if rect_y == 0:
        rect_y = height - hbox
    if rect_y == height:
        rect_y = 0

    if rect_x == 0:
        rect_x = width - wbox
    if rect_x == width:
        rect_x = 0


    pygame.display.flip()
