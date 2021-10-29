#Sherry Zhang
#10/25/21

import pygame, os, random
from pygame.locals import *
os.system('clear')

pygame.init()

def display_text(msg, x, y, font):
    text = font.render(msg, 5, colors[0])
    if x == "mid":
        name = window.blit(text, (width/2 - text.get_width()/2, y))

    else:
        name = window.blit(text, (width - text.get_width(), height - text.get_height()))

    return name

colors = [(0,0,0), (255,0,0), (0,0,255)]
background_colors = [(255,255,255), (0,255,0), (169,77,255), (255,160,77)]

background = 0
obj_1_color = 0
obj_2_color = obj_1_color + 1

width, height = 500, 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Setting Window")

TITLE_FONT = pygame.font.SysFont("Times New Roman", 80)
SUBTITLE_FONT = pygame.font.SysFont("Times New Roman", 40)

run = True

screen_size_x = 110
back_color_x = screen_size_x + 50
obj_color_x = back_color_x + 50
sound_x = obj_color_x + 50
play_x = sound_x + 50

menu = True
settings = False
game = False

rect_y = height/2
rect_x = width/2
circle_x = width/4
circle_y = height/4

wbox = 30
hbox = 30
radius = wbox/2

score = 3
speed = 5
key_list = [[K_UP, 0,0,0, -speed], [K_DOWN, 0,0,0,speed], [K_RIGHT, 0,0,speed,0], [K_LEFT, 0,0,-speed,0], 
            [K_w, 0,-speed,0,0], [K_s, 0,speed,0,0], [K_a, -speed,0,0,0], [K_d, speed,0,0,0]]

while run:

    mouse_pos = pygame.mouse.get_pos()
    left_pressed, middle_pressed, right_pressed = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if menu:
        window.fill(background_colors[background])

        display_text("Menu", "mid", 10, TITLE_FONT)
        instructions = display_text("Instructions", "mid", screen_size_x, SUBTITLE_FONT)
        settings_text = display_text("Settings", "mid", back_color_x, SUBTITLE_FONT)
        play = display_text("Play", "mid", play_x, SUBTITLE_FONT)

        if left_pressed:
            if play.collidepoint(mouse_pos):
                menu = False
                game = True
            
            elif settings_text.collidepoint(mouse_pos):
                settings = True
                menu = False

    if settings:
        window.fill(background_colors[background])

        display_text("Settings", "mid", 10, TITLE_FONT)
        screen_size = display_text("Screen Size", "mid", screen_size_x, SUBTITLE_FONT)
        background_color = display_text("Background Color", "mid", back_color_x, SUBTITLE_FONT)
        obj_color = display_text("Object Color", "mid", obj_color_x, SUBTITLE_FONT)
        sound = display_text("Sound On/Off", "mid", sound_x, SUBTITLE_FONT)
        play = display_text("Play", "mid", play_x, SUBTITLE_FONT)

        back = display_text("Back", 'side', 'side', SUBTITLE_FONT)

        if left_pressed:
            if screen_size.collidepoint(mouse_pos):
                width, height = 700, 700
                pygame.display.set_mode((width, height))
            
            elif background_color.collidepoint(mouse_pos):
                if background < 3:
                    background += 1
                elif background == 3:
                    background = 0
            
            elif obj_color.collidepoint(mouse_pos):
                if obj_1_color == len(colors) - 2:
                    obj_2_color = 0
                    obj_1_color += 1
                elif obj_1_color == len(colors) - 1:
                    obj_1_color = 0
                    obj_2_color = 1

                else:
                    obj_1_color += 1
                    obj_2_color += 1
            
            if back.collidepoint(mouse_pos):
                settings = False
                menu = True
        
        pygame.draw.rect(window, colors[obj_1_color], (width/2 - 50, play_x + 50, hbox, wbox))
        circle = pygame.draw.circle(window, colors[obj_2_color], (width/2 + 25, play_x + 50 + radius), radius)
    
    elif game:
        pygame.time.delay(10)

        window.fill(background_colors[background])
        left_pressed, middle_pressed, right_pressed = pygame.mouse.get_pressed()

        rect = pygame.draw.rect(window, colors[obj_1_color], (rect_x, rect_y, wbox, hbox))
        circle = pygame.draw.circle(window, colors[obj_2_color], (circle_x, circle_y), radius)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keyPressed = pygame.key.get_pressed()

        for i in key_list:
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
            game = False
            settings = True
            run = False

        if rect.colliderect(circle):
            score -= 1
            radius += 7
            rect_x = random.randint(0, width - wbox)
            rect_y = random.randint(0, height - hbox)
            
    pygame.display.flip()
