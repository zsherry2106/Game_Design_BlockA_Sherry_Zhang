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

#[key, circlex, circley, rectx, recy]
test = [[K_UP, 0,0,0, -speed], [K_DOWN, 0,0,0,speed], [K_RIGHT, 0,0,speed,0], [K_LEFT, 0,0,-speed,0], 
        [K_w, 0,-speed,0,0], [K_s, 0,speed,0,0], [K_a, -speed,0,0,0], [K_d, speed,0,0,0]]
while running:
    pygame.time.delay(10)
    window.fill(color)
    left_pressed, middle_pressed, right_pressed = pygame.mouse.get_pressed()

    rect = pygame.draw.rect(window, colors.get('blue'), (rect_x, rect_y, wbox, hbox))
    circle = pygame.draw.circle(window, colors.get('red'), (circle_x, circle_y), radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keyPressed = pygame.key.get_pressed()

    for i in test:
        if keyPressed[i[0]]:
            circle_x += i[1]
            circle_y += i[2]
            rect_x += i[3]
            rect_y += i[4]
    
    if rect_x < 0:
        rect_x = width
    elif rect_x > width:
        rect_x = 0
    
    if rect_y < 0:
        rect_y = height
    elif rect_y > height:
        rect_y = 0
    
    if circle_x < radius:
        circle_x = radius
    elif circle_x > width - radius:
        circle_x = width - radius

    if circle_y < radius:
        circle_y = radius
    elif circle_y > height - radius:
        circle_y = height - radius

    
    if score == 0:
        print("Blue Lost!")
        running = False

    if rect.colliderect(circle):
        score -= 1
        radius += 7
        rect_x = random.randint(0, width - wbox)
        rect_y = random.randint(0, height - hbox)

    pygame.display.flip()
