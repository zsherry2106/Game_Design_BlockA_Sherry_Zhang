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
# color = random.choice(list(colors.keys()))
color = 'white'
color = colors.get(color)

window.fill(color)
pygame.display.set_caption("Game Window")
running = True


rect_y = height/2
rect_x = width/2

wbox = 30
hbox = 30


radius = wbox/2
circle_x = width/4
circle_y = height/4

score = 3

speed = 5
# circle = pygame.circle(width/4, height/4, radius)

while running:
    pygame.time.delay(10)
    window.fill(color)
    left_pressed, middle_pressed, right_pressed = pygame.mouse.get_pressed()
    # mouse = pygame.mouse.get_pos()
    # print(mouse
    rect = pygame.draw.rect(window, colors.get('blue'), (rect_x, rect_y, wbox, hbox))
    circle = pygame.draw.circle(window, colors.get('red'), (circle_x, circle_y), radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keyPressed = pygame.key.get_pressed()

    if keyPressed[pygame.K_UP]:
        rect_y -= speed
    elif keyPressed[pygame.K_DOWN]:
        rect_y += speed

    if keyPressed[pygame.K_RIGHT]:
        rect_x += speed
    elif keyPressed[pygame.K_LEFT]:
        rect_x -= speed

    if rect_y <= 0:
        rect_y = height - hbox
    elif rect_y >= height:
        rect_y = 0

    if rect_x <= 0:
        rect_x = width - wbox
    elif rect_x >= width:
        rect_x = 0
    

    if keyPressed[pygame.K_w] and circle_y > radius:
        circle_y -= speed
    elif keyPressed[pygame.K_s] and circle_y < height - radius:
        circle_y += speed

    if keyPressed[pygame.K_a] and circle_x > radius:
        circle_x -= speed
    elif keyPressed[pygame.K_d] and circle_x <  width - radius:
        circle_x += speed

    
    if score == 0:
        print("Blue Lost!")
        running = False

    if rect.colliderect(circle):
        score -= 1
        radius += 7
        rect_x = random.randint(0, width - wbox)
        rect_y = random.randint(0, height - hbox)

    pygame.display.flip()
