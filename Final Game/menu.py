#Sherry Zhang
#10/25/21

import pygame, os, random, time
from pygame.locals import *
os.system('cls')


pygame.init()

#func to display text
def display_text(msg_list):
    y = 10
    msg_dict = {}

    for i in range(len(msg_list)):
        if msg_list[i] == "Back":
            text = SUBTITLE_FONT.render(msg_list[i], 5, (0,0,0))
            y = HEIGHT - 50
            msg_dict[msg_list[i]] = window.blit(text, (WIDTH/2 - text.get_width()/2, y))
        
        elif i == 0:
            text = TITLE_FONT.render(msg_list[i], 5, (0,0,0))
            msg_dict[msg_list[i]] = window.blit(text, (WIDTH/2 - text.get_width()/2, y))
            y += 100
            
        else:
            text = SUBTITLE_FONT.render(msg_list[i], 5, (0,0,0))
            msg_dict[msg_list[i]] = window.blit(text, (WIDTH/2 - text.get_width()/2, y))
            y += 50

    return msg_dict

#Display background color options
def background_color_display():
    x = WIDTH/len(background_colors)
    msg_dict = {}
    
    for i in background_colors:
        color = background_colors[i]
        rect = pygame.draw.rect(window, color, (x, HEIGHT/2, wbox, hbox))
        pygame.draw.rect(window, (0,0,0), (x, HEIGHT/2, wbox, hbox), 1)
        x += 100

        msg_dict[i] = rect
    
    return msg_dict

#Display sprites for sprite options
def display_sprite_options():
    #Append displayed sprites for later interaction/selection (check collide)
    sprite_list = []
    y = 200

    for sprite in sprite_options:
        window.blit(sprite, (WIDTH/2 - sprite.get_width()/2, y))
        y += 100
    
    # return sprite_list

#Display scoreboard from txt file
def display_scoreboard(level):
    txt = [f'Scoreboard Level{level}']
    current_folder = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(current_folder, f'scoreboard{level}.txt'), "r") as myfile:
        for line in myfile:
            if line != "\n":
                txt.append(line)
    txt.append('Back')

    return txt

#Colors
#           Black   Red         Blue
colors = [(255,0,0), (0,0,255)]
background_colors = {'white': (255,255,255), 'green': (0,255,0), 'light bl': (158, 214, 219), 'pink': (235, 192, 219)}

sprite_options = [pygame.image.load("Final Game\Images\sprite_pink\pinkL1.png")]

#Set default colors
background = 'white'
obj_1_color = colors[0]
obj_2_color = colors[1]

#Set page width/height - create variables to change later
WIDTH, HEIGHT = 700, 700
window = pygame.display.set_mode((WIDTH, HEIGHT))

#fonts needed for display
TITLE_FONT = pygame.font.SysFont("Times New Roman", 80)
SUBTITLE_FONT = pygame.font.SysFont("Times New Roman", 40)

#Lists of messages to display on pages
menu_text = ["Menu", "Instructions",  "Settings", "Scoreboard", "Level 1", "Level 2", "Level 3", "Exit"]
settings_text = ['Settings', "Screen Size", "Background Color", "Sprite", "Sound On/Off", "Back"]
screen_size_text = ["Screen Size", "800 by 800", "700 by 700", "600 by 600", "Back"]

run = True

background_image = pygame.image.load("Final Game/Images/background.png")

scoreboard_main_text = ['Scoreboard', 'Level 1', 'Level 2', 'Level 3', 'Back']

#pos for text
screen_size_x = 110
back_color_x = screen_size_x + 50
obj_color_x = back_color_x + 50
sound_x = obj_color_x + 50
play_x = sound_x + 50

#sets what page we want shown
page = 'menu'

#variables for game
rect_y = HEIGHT/2
rect_x = WIDTH/2
circle_x = WIDTH/4
circle_y = HEIGHT/4
wbox = 30
hbox = 30
radius = wbox/2
score = 3
speed = 5

#Key list for moving obj in game
key_list = [[K_UP, 0,0,0, -speed], [K_DOWN, 0,0,0,speed], [K_RIGHT, 0,0,speed,0], [K_LEFT, 0,0,-speed,0], 
            [K_w, 0,-speed,0,0], [K_s, 0,speed,0,0], [K_a, -speed,0,0,0], [K_d, speed,0,0,0]]

# name = input("Enter your name: ")
name = 'Sherry'
while run:
    window.fill(background_colors[background])
    #Set mouse pos so that it doesn't click through to next page
    mouse_pos = [-1,-1]
    left_pressed, middle_pressed, right_pressed = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            mouse_pos = event.pos
        
    if page == 'menu':
        pygame.display.set_caption("Menu")

        menu_msg = display_text(menu_text)

        if menu_msg['Level 1'].collidepoint(mouse_pos):
            page = 'level_1'
        
        elif menu_msg['Level 2'].collidepoint(mouse_pos):
            page = 'level_2'

        elif menu_msg['Level 3'].collidepoint(mouse_pos):
            page = 'level_3'
              
        elif menu_msg["Instructions"].collidepoint(mouse_pos):
            page = 'instructions'
        
        elif menu_msg["Settings"].collidepoint(mouse_pos):
            page = 'settings'
        
        elif menu_msg['Scoreboard'].collidepoint(mouse_pos):
            page = 'scoreboard'
        
        elif menu_msg["Exit"].collidepoint(mouse_pos):
            run = False

    elif page == 'instructions':
        pygame.display.set_caption("Instructions")
        instructions_msg = display_text(["Instructions", "Collect the eggs as quick as possible", 
                                         'Use the arrow keys to move', 'Back'])

        if instructions_msg['Back'].collidepoint(mouse_pos):
            page = 'menu'

    elif page == 'settings':
        pygame.display.set_caption("Settings")

        settings_msg = display_text(settings_text)

        if settings_msg["Screen Size"].collidepoint(mouse_pos):
            page = 'screen_size'
        
        elif settings_msg["Background Color"].collidepoint(mouse_pos):  
            page = 'background'
        
        elif settings_msg["Sprite"].collidepoint(mouse_pos):
            page = 'sprite'
        
        if settings_msg["Back"].collidepoint(mouse_pos):
            page = 'menu'
    
    elif page == 'screen_size':
        pygame.display.set_caption("Screen Size Settings")

        screen_size_msg = display_text(screen_size_text)

        if screen_size_msg["800 by 800"].collidepoint(mouse_pos):
            WIDTH, HEIGHT = 800, 800
        
        elif screen_size_msg["700 by 700"].collidepoint(mouse_pos):
            WIDTH, HEIGHT = 700, 700
        
        elif screen_size_msg["600 by 600"].collidepoint(mouse_pos):
            WIDTH, HEIGHT = 600, 600
        
        elif screen_size_msg["Back"].collidepoint(mouse_pos):
            page = 'settings'
        
        # window = pygame.display.set_mode((WIDTH, HEIGHT))

    elif page == 'background':
        pygame.display.set_caption("Background Color Settings")

        background_rect = background_color_display()
        back_text = display_text(['Background Color', 'Back'])

        if back_text["Back"].collidepoint(mouse_pos):
            page = 'settings'
        
        elif background_rect['white'].collidepoint(mouse_pos):
            background = 'white'

        elif background_rect['green'].collidepoint(mouse_pos):
            background = 'green'

        elif background_rect['light bl'].collidepoint(mouse_pos):
            background = 'light bl'

        elif background_rect['pink'].collidepoint(mouse_pos):
            background = 'pink'
    
    elif page == 'sprite':
        pygame.display.set_caption("Sprite Options")
        obj_color_msg = display_text(["Sprite", 'Back'])

        display_sprite_options()
        # print(sprite_options)

        # for i in sprite_options:
        #     if i[0].collidepoint(mouse_pos):
        #         obj_1_color = i[1]
        
        # for circle in circle_list:
        #     if circle[0].collidepoint(mouse_pos):
        #         obj_2_color = circle[1]

        if obj_color_msg['Back'].collidepoint(mouse_pos):
            page = 'settings'
        
        # window.blit()

    elif page == 'scoreboard':
        pygame.display.set_caption("Scoreboard Selection")
        scoreboard_msg = display_text(scoreboard_main_text)

        if scoreboard_msg['Back'].collidepoint(mouse_pos):
            page = 'menu'
        
        elif scoreboard_msg['Level 1'].collidepoint(mouse_pos):
            page = 'score_level1'
        
        elif scoreboard_msg['Level 2'].collidepoint(mouse_pos):
            page = 'score_level2'
        
        elif scoreboard_msg['Level 3'].collidepoint(mouse_pos):
            print('test')
            page = 'score_level3'
    
    elif page == 'score_level1':
        pygame.display.set_caption("Scoreboard Level 1")
        score_level1_text = display_scoreboard(1)
        score_level1_msg = display_text(score_level1_text)

        if score_level1_msg['Back'].collidepoint(mouse_pos):
            page = 'scoreboard'
    
    elif page == 'score_level2':
        pygame.display.set_caption("Scoreboard Level 2")
        score_level2_text = display_scoreboard(2)
        score_level2_msg = display_text(score_level2_text)

        if score_level2_msg['Back'].collidepoint(mouse_pos):
            page = 'scoreboard'
    
    elif page == 'score_level3':
        pygame.display.set_caption("Scoreboard Level 3")
        score_level3_text = display_scoreboard(3)
        score_level3_msg = display_text(score_level3_text)

        if score_level3_msg['Back'].collidepoint(mouse_pos):
            page = 'scoreboard'

    elif page == 'level_1':
        import level1
        level1.level_1_page(name)
        page = 'menu'
    
    elif page == 'level_2':
        import level2
        level2.level_2_page(name)
        page = 'menu'

    elif page == 'level_3':
        import level3
        level3.level_3_page(name)
        page = 'menu'

    pygame.display.flip()

pygame.quit()
