#Sherry Zhang
#10/25/21

#pygame fonts

import pygame as pygame, os
os.system('clear')

pygame.init()

WIDTH, HEIGHT = 600, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Setting Window")

#pygame font has 4 parameters: name, size, bold, and italic
#bold/italic automatically false
TITLE_FONT = pygame.font.SysFont("Times New Roman", 80)
SUBTITLE_FONT = pygame.font.SysFont("Times New Roman", 40)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

run = True

def display_text(msg, height, font):
    #takes text, thickness, color
    # pygame.time.delay(1000)
    text = font.render(msg, 5, BLACK)
    window.blit(text, (WIDTH/2 - text.get_width()/2, height))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(WHITE)
    
    display_text("Settings", 10, TITLE_FONT)
    display_text("Screen Size", 110, SUBTITLE_FONT)
    display_text("Background Color", 160, SUBTITLE_FONT)
    display_text("Object Color", 210, SUBTITLE_FONT)
    display_text("Sound On/Off", 260, SUBTITLE_FONT)

    pygame.display.flip()

    pygame.display.flip()
