#Sherry Zhang
#10/25/21

#Final game

import pygame, random, os, time

os.system('clear')
pygame.init()

colors = {'black': (0, 0, 0),
          'white': (255, 255, 255),
          'red': (255, 0, 0),
          'blue': (0, 0, 255),
          'green': (0, 255, 0)}

WIDTH, HEIGHT = 600, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))

SETTINGS_FONT = pygame.font.SysFont("Times New Roman", 40)

def display_text(msg, font, thickness, color):
    text = font.render(msg, thickness, color)
    return text

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    background_color = colors.get('white')
    window.fill(background_color)

    settings_text = display_text('Settings', SETTINGS_FONT, 5, colors.get('black'))
    window.blit(settings_text, (WIDTH/2 - settings_text.get_width()/2, 0))

    pygame.display.flip()
