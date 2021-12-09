#Sherry Zhang
#11/18/21

#Level 3 of Final Game
#Test

import os, pygame, time
from pygame.locals import *

os.system('cls')
pygame.init()

def level_3_page(name):
    WIDTH, HEIGHT = 700, 700

    pygame.display.set_caption("Level 3")
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
    
    portal_right_image = pygame.image.load("Final Game\Images\portalR.png")
    portal_left_image = pygame.image.load("Final Game\Images\portalL.png")
    portal_up_image = pygame.image.load("Final Game\Images\portalD.png")
    portal_down_image = pygame.image.load("Final Game\Images\portalU.png")

    #image, x, y
    portal_image_list = [[portal_down_image, 0, HEIGHT - portal_down_image.get_height(), 0, 600], [portal_left_image, 100, 200, 121, 210],
                         [portal_right_image, WIDTH - portal_right_image.get_width(), 200, 610, 210], [portal_down_image, 600, HEIGHT - portal_down_image.get_height(), 600, 600],
                         [portal_down_image, 500, HEIGHT - portal_down_image.get_height(), 510, 610], [portal_right_image, 600 - portal_right_image.get_width(), 0, 510, 0],
                         [portal_down_image, 200, 400 - portal_down_image.get_height(), 210, 400], [portal_right_image, 500 - portal_right_image.get_width(), 0, 400, 0],
                         [portal_up_image, 100, 0, 110, 130], [portal_right_image, WIDTH - portal_right_image.get_width(), 0, 610, 0]
                         ]
    portal_list = []

    for portal in portal_image_list:
        portal_list.append(window.blit(portal[0], (portal[1], portal[2])))

    egg_image = pygame.image.load("Final Game/Images/egg1.png")

    #check if sprite collides with walls/boundaries
    def check_collide(sprite, image, x, y, direction):
        for i in range(len(boundary_list)):
            if sprite.colliderect(boundary_list[i]):
                if direction == 'left':
                    x = boundary_coordinate_list[i][0] + 7 + boundary_coordinate_list[i][2]

                elif direction == 'right':
                    x = boundary_coordinate_list[i][0] - image.get_width() - 7

                elif direction == 'up':
                    y = boundary_coordinate_list[i][1] + boundary_coordinate_list[i][3]

                elif direction == 'down':
                    y = boundary_coordinate_list[i][1] - image.get_height() - 7

        return x, y

    #function to operate portals - if collide with one go to the other one
    def portals(sprite, x, y):
        for i in range(len(portal_list)):
            if i % 2 == 0:
                if sprite.colliderect(portal_list[i]):
                    x = portal_image_list[i + 1][3]
                    y = portal_image_list[i + 1][4]
            
            else:
                if sprite.colliderect(portal_list[i]):
                    x = portal_image_list[i - 1][3]
                    y = portal_image_list[i - 1][4]

        return x, y

    run = True
    #Variables for sprite position
    sprite_pos_x = 0
    sprite_pos_y = 0

    sprite_direction = "right"

    #list of coordinates for walls
    #x, y, width, height
    boundary_coordinate_list = [[100, 0, 5, 500], [100, 200, 400, 5], [100, 500, 600, 5],
                                [500, 500, 5, 200], [200, 200, 5, 200], [200, 400, 400, 5],
                                [600, 0, 5, 405], [600, 200, 100, 5], [500, 0, 5, 305],
                                [400, 300, 5, 100]]
    #list that contains rect for all boundaries
    boundary_list = []
    #Append physical rect to boundary_list
    for i in boundary_coordinate_list:
        boundary_list.append(pygame.draw.rect(window, (169, 177, 131), (i[0], i[1], i[2], i[3])))

    #variable to control speed of sprite
    speed = 2

    #Settings for timer including start time + font
    time_start = pygame.time.get_ticks()
    TIMER_FONT = pygame.font.SysFont("Times New Roman", 40)

    #sprite_num - used to calculate which sprite to use out of list of 3
    sprite_num = 0

    while run:
        window.blit(background, (0,0))

        for portal in portal_image_list:
            window.blit(portal[0], (portal[1], portal[2]))

        time_passed = pygame.time.get_ticks() - time_start
        stopwatch = TIMER_FONT.render(str(time_passed / 1000), True, (0,0,0))
        window.blit(stopwatch, (0, 0))

        egg = window.blit(egg_image, (611, 100))
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
                sprite_pos_x -= speed
                sprite_num += 1
                sprite_direction = 'left'
            
            elif keyPressed[K_RIGHT]:
                sprite_pos_x += speed
                sprite_num += 1
                sprite_direction = 'right'
            
            elif keyPressed[K_UP]:
                sprite_pos_y -= speed
                sprite_num += 1
                sprite_direction = 'up'
            
            elif keyPressed[K_DOWN]:
                sprite_num += 1
                sprite_pos_y += speed
                sprite_direction = 'down'
        
        #if hits borders - stop moving and reset position
        if sprite_pos_x < 0:
            sprite_pos_x = 1
        
        elif sprite_pos_x + image_current.get_width() > WIDTH:
            sprite_pos_x = WIDTH - image_current.get_width()
        
        if sprite_pos_y < 0:
            sprite_pos_y = 1
        
        elif sprite_pos_y + image_current.get_height() > HEIGHT:
            sprite_pos_y = HEIGHT- image_current.get_height()
        

        #draw walls/boundaries
        for i in boundary_coordinate_list:
            pygame.draw.rect(window, (169, 177, 131), (i[0], i[1], i[2], i[3]))

        #Check if egg has been hit
        if egg.colliderect(sprite_current):
            #add passed time to scoreboard file
            current_folder = os.path.dirname(os.path.abspath(__file__))
            with open(os.path.join(current_folder, 'scoreboard3.txt'), "w") as myfile:
                myfile.write(f"\n{name}- Level3: {time_passed/1000}")
            
            run = False

        #Call portals function
        sprite_pos_x, sprite_pos_y = portals(sprite_current, sprite_pos_x, sprite_pos_y)
        
        text = TIMER_FONT.render('Back', 5, (0,0,0))
        back_text = window.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT - 50))

        sprite_pos_x, sprite_pos_y = check_collide(sprite_current, image_current, sprite_pos_x, sprite_pos_y, sprite_direction)

        if pygame.mouse.get_pressed()[0]:
            if back_text.collidepoint(pygame.mouse.get_pos()):
                run = False

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
