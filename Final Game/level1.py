#Sherry Zhang
#11/18/21

#Level 1 of Final Game
#Test

import os, pygame, time
from pygame.locals import *

os.system('cls')
pygame.init()

def level_1_page(name):
    WIDTH, HEIGHT = 700, 700

    window = pygame.display.set_mode((WIDTH, HEIGHT))

    background = pygame.image.load("Final Game/Images/background.png")
    pink_sprite_l = [pygame.image.load("Final Game/Images/sprite_pink/pinkL1.png"), 
                    pygame.image.load("Final Game/Images/sprite_pink/pinkL2.png"), 
                    pygame.image.load("Final Game/Images/sprite_pink/pinkL3.png")]
    pink_sprite_r = [pygame.image.load("Final Game/Images/sprite_pink/pinkR1.png"), 
                    pygame.image.load("Final Game/Images/sprite_pink/pinkR2.png"), 
                    pygame.image.load("Final Game/Images/sprite_pink/pinkR3.png")]
    pink_sprite_u = [pygame.image.load("Final Game/Images/sprite_pink/pinkU1.png"), 
                    pygame.image.load("Final Game/Images/sprite_pink/pinkU2.png"), 
                    pygame.image.load("Final Game/Images/sprite_pink/pinkU3.png")]

    egg_image = pygame.image.load("Final Game/Images/egg1.png")

    #check if sprite collides with walls/boundaries
    def check_collide(sprite, x, y, direction):
        for i in boundary_list:
            if sprite.colliderect(i):
                print("test")
                x += direction_dict[direction][0]
                y += direction_dict[direction][1]

        return x, y


    run = True
    #Variables for sprite position
    sprite_pos_x = 0
    sprite_pos_y = 600

    collide_delay = 0

    image = pink_sprite_l[0]

    sprite_direction = "right"

    direction_dict = {'up': [0, 5], 'down': [0, -5], 'left': [5,0], 'right': [-5,0]}


    time_start = pygame.time.get_ticks()
    TIMER_FONT = pygame.font.SysFont("Times New Roman", 40)

    #sprite_num - used to calculate which sprite to use out of list of 3
    sprite_num = 0

    #list of coordinates for walls
    #x, y, width, height
    boundary_coordinate_list = [[100, 100, 5, 600], [200, 100, 5, 500], [200, 100, 300, 5], 
                                [200, 400, 100, 5], [300, 200, 200, 5], [300, 300, 100, 5], 
                                [400, 300, 5, 205], [300, 500, 100, 5], [300, 500, 5, 200],
                                [500, 100, 5, 500], [400, 600, 105, 5], [500, 400, 100, 5],
                                [600, 0, 5, 600]]
    #list that contains rect for all boundaries
    boundary_list = []

    while run:
        window.blit(background, (0,0))


        time_passed = pygame.time.get_ticks() - time_start
        stopwatch = TIMER_FONT.render(str(time_passed / 1000), True, (0,0,0))
        window.blit(stopwatch, (0, 0))

        egg = window.blit(egg_image, (611, 0))
        # print(pygame.mouse.get_pos())
        keyPressed = pygame.key.get_pressed()

        if (sprite_num // 15) == len(pink_sprite_l):
            sprite_num = 0

        #Choose sprite direction and then choose image
        if sprite_direction == 'left' or sprite_direction == 'down':
            image_current = pink_sprite_l[sprite_num // 15]

        elif sprite_direction == 'right':
            image_current = pink_sprite_r[sprite_num // 15]

        elif sprite_direction == 'up':
            image_current = pink_sprite_u[sprite_num // 15]

        sprite_current = window.blit(image_current, (sprite_pos_x, sprite_pos_y))


        if 0 <= sprite_pos_x <= WIDTH - image_current.get_width() and 0 <= sprite_pos_y <= HEIGHT - image_current.get_height():   
            if keyPressed[K_LEFT]:
                sprite_pos_x -= 5
                sprite_num += 1
                sprite_direction = 'left'
            
            elif keyPressed[K_RIGHT]:
                sprite_pos_x += 5
                sprite_num += 1
                sprite_direction = 'right'
            
            elif keyPressed[K_UP]:
                sprite_pos_y -= 5
                sprite_num += 1
                sprite_direction = 'up'
            
            elif keyPressed[K_DOWN]:
                sprite_num += 1
                sprite_pos_y += 5
                sprite_direction = 'down'
        
        if 0 > sprite_pos_x:
            sprite_pos_x = 1
        
        elif sprite_pos_x + image_current.get_width() > WIDTH:
            sprite_pos_x = WIDTH - 1
        
        if 0 > sprite_pos_y:
            sprite_pos_y = 1
        
        elif sprite_pos_y + image_current.get_height() > HEIGHT:
            sprite_pos_y = HEIGHT -1
        

        #draw walls/boundaries
        for i in boundary_coordinate_list:
            boundary_list.append(pygame.draw.rect(window, (169, 177, 131), (i[0], i[1], i[2], i[3])))


        #Check if egg has been hit
        if egg.colliderect(sprite_current):
            run = False
        
        sprite_pos_x, sprite_pos_y = check_collide(sprite_current, sprite_pos_x, sprite_pos_y, sprite_direction)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

    current_folder = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(current_folder, 'scoreboard.txt'), "a") as myfile:
        myfile.write(f"\n{name}: {time_passed/1000}")
