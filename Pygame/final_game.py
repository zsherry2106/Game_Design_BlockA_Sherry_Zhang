#Sherry Zhang
#10/25/21

#pygame fonts

import pygame, os, random
from pygame.locals import *
os.system('clear')

pygame.init()

def display_text(msg, y, font):
    #takes text, thickness, color
    # pygame.time.delay(1000)
    text = font.render(msg, 5, colors.get('black'))
    name = window.blit(text, (width_menu/2 - text.get_width()/2, y))
    return name

def option_text(msg, x, y, font):
    text = font.render(msg, 5, colors.get('black'))
    name = window.blit(text, (x, y))
    return name

colors = {'black':(0,0,0), 
          'red':(255,0,0), 
          'green':(0,255,0), 
          'blue':(0,0,255), 
          'white':(255,255,255), 
          'purple':(169,77,255),
          'orange':(255,160,77)
          }

width_menu, height_menu = 600, 600
window = pygame.display.set_mode((width_menu, height_menu))
pygame.display.set_caption("Setting Window")

width_game, height_game = 600, 600
color_game = colors.get('white')

TITLE_FONT = pygame.font.SysFont("Times New Roman", 80)
SUBTITLE_FONT = pygame.font.SysFont("Times New Roman", 40)

run = True

screen_size_x = 110
back_color_x = 160
menu = True
game = False

rect_y = height_game/2
rect_x = width_game/2
circle_x = width_game/4
circle_y = height_game/4
while run:

    mouse_pos = pygame.mouse.get_pos()
    left_pressed, middle_pressed, right_pressed = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if menu:
        obj_color_x = back_color_x + 50
        sound_x = obj_color_x + 50
        play_x = sound_x + 50

        window.fill(colors.get('white'))

        settings = display_text("Settings", 10, TITLE_FONT)
        screen_size = display_text("Screen Size", screen_size_x, SUBTITLE_FONT)
        background_color = display_text("Background Color", back_color_x, SUBTITLE_FONT)
        obj_color = display_text("Object Color", obj_color_x, SUBTITLE_FONT)
        sound = display_text("Sound On/Off", sound_x, SUBTITLE_FONT)
        play = display_text("Play", play_x, SUBTITLE_FONT)

        if left_pressed:
            if play.collidepoint(mouse_pos):
                menu = False
                game = True

            elif screen_size.collidepoint(mouse_pos):
                back_color_x = 210
                # width_game, height_game = 
    
    elif game:
        pygame.time.delay(10)
        wbox = 30
        hbox = 30
        radius = wbox/2

        score = 3
        speed = 5

        window.fill(color_game)
        left_pressed, middle_pressed, right_pressed = pygame.mouse.get_pressed()

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
            rect_y = height_game - hbox
        elif rect_y >= height_game:
            rect_y = 0

        if rect_x <= 0:
            rect_x = width_game - wbox
        elif rect_x >= width_game:
            rect_x = 0
        

        if keyPressed[pygame.K_w] and circle_y > radius:
            print('test')
            circle_y -= speed
        elif keyPressed[pygame.K_s] and circle_y < height_game - radius:
            circle_y += speed

        if keyPressed[pygame.K_a] and circle_x > radius:
            circle_x -= speed
        elif keyPressed[pygame.K_d] and circle_x <  width_game - radius:
            circle_x += speed

        
        if score == 0:
            print("Blue Lost!")
            running = False

        if rect.colliderect(circle):
            score -= 1
            radius += 7
            rect_x = random.randint(0, width_game - wbox)
            rect_y = random.randint(0, height_game - hbox)
            
    pygame.display.flip()
