#Sherry Zhang
#10/25/21

import pygame, os, random, time
from pygame.locals import *
os.system('clear')

pygame.init()

def display_text(msg, y, font, color):
    text = font.render(msg, 5, color)
    name = window.blit(text, (width/2 - text.get_width()/2, y))

    return name

colors = [(0,0,0), (255,0,0), (0,0,255)]
background_colors = [(255,255,255), (0,255,0), (169,77,255), (255,160,77)]

background = 0
obj_1_color = 0
obj_2_color = obj_1_color + 1

width, height = 600, 600
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

page = 'menu'

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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    if page == 'menu':
        window.fill(background_colors[background])

        menu_text = ["Menu", "Instructions",  "Settings", "Play"]

        display_text("Menu", 10, TITLE_FONT, colors[0])
        instructions = display_text("Instructions", 110, SUBTITLE_FONT, colors[0])
        settings_text = display_text("Settings", 160, SUBTITLE_FONT, colors[0])
        play = display_text("Level 1", 210, SUBTITLE_FONT, colors[0])
        display_text("Level 2", 260, SUBTITLE_FONT, colors[0])
        exit_menu = display_text("Exit", 310, SUBTITLE_FONT, colors[0])

        if pygame.mouse.get_pressed()[0]:
            if play.collidepoint(mouse_pos):
                page = 'level_1'
            
            elif settings_text.collidepoint(mouse_pos):
                page = 'settings'
                pygame.mouse.set_pos(mouse_pos[0] - 10, mouse_pos[1] - 10)
            
            elif exit_menu.collidepoint(mouse_pos):
                run = False

    elif page == 'settings':
        window.fill(background_colors[background])

        display_text("Settings", 10, TITLE_FONT, colors[0])
        screen_size = display_text("Screen Size", screen_size_x, SUBTITLE_FONT, colors[0])
        background_color = display_text("Background Color", back_color_x, SUBTITLE_FONT, colors[0])
        obj_color = display_text("Object Color", obj_color_x, SUBTITLE_FONT, colors[0])
        sound = display_text("Sound On/Off", sound_x, SUBTITLE_FONT, colors[0])

        back = display_text("Back", height -50, SUBTITLE_FONT, colors[0])

        pygame.draw.rect(window, colors[obj_1_color], (width/2 - 50, play_x + 50, hbox, wbox))
        circle = pygame.draw.circle(window, colors[obj_2_color], (width/2 + 25, play_x + 50 + radius), radius)

        if pygame.mouse.get_pressed()[0]:
            if screen_size.collidepoint(mouse_pos):
                pygame.mouse.set_pos(mouse_pos[0] - 10, mouse_pos[1] - 10)
                page = 'screen_size'
            
            elif background_color.collidepoint(mouse_pos):
                pygame.mouse.set_pos(mouse_pos[0] - 10, mouse_pos[1] - 10)
                page = 'background'
            
            if back.collidepoint(mouse_pos):
                page = 'menu'
    
    elif page == 'screen_size':
        window.fill(background_colors[background])
        display_text("Screen Size", 10, TITLE_FONT, colors[0])
        eight = display_text("800 by 800", screen_size_x, SUBTITLE_FONT, colors[0])
        seven = display_text("700 by 700", back_color_x, SUBTITLE_FONT, colors[0])
        six = display_text("600 by 600", obj_color_x, SUBTITLE_FONT, colors[0])

        back = display_text("Back", height - 50, SUBTITLE_FONT, colors[0])

        if pygame.mouse.get_pressed()[0]:
            if eight.collidepoint(mouse_pos):
                width, height = 800, 800
            
            elif seven.collidepoint(mouse_pos):
                width, height = 700, 700
            
            elif six.collidepoint(mouse_pos):
                width, height = 600, 600
            
            elif back.collidepoint(mouse_pos):
                page = 'settings'
        
        window = pygame.display.set_mode((width, height))

    elif page == 'background':
        window.fill(background_colors[background])
        display_text("Background Color", 10, TITLE_FONT, colors[0])

        back = display_text("Back", height - 50, SUBTITLE_FONT, colors[0])

        if pygame.mouse.get_pressed()[0]:
            if back.collidepoint(mouse_pos):
                page = 'settings'

    elif page == 'level_1':
        pygame.time.delay(10)

        window.fill(background_colors[background])

        rect = pygame.draw.rect(window, colors[obj_1_color], (rect_x, rect_y, wbox, hbox))
        circle = pygame.draw.circle(window, colors[obj_2_color], (circle_x, circle_y), radius)
        
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
            page = 'menu'

        if rect.colliderect(circle):
            score -= 1
            radius += 7
            rect_x = random.randint(0, width - wbox)
            rect_y = random.randint(0, height - hbox)
            
    pygame.display.flip()
