#Sherry Zhang
#11/18/21

#Level 2 of Final Game
#Test

import os, pygame, time
from pygame.locals import *

os.system('cls')
pygame.init()

def level_2_page(name, sprite_choice):
    WIDTH, HEIGHT = 700, 700

    pygame.display.set_caption("Level 2")
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    background = pygame.image.load("Final Game/Images/background.png")

    sprite_l = [pygame.image.load(f"Final Game/Images/sprites/{sprite_choice}L1.png"), 
                pygame.image.load(f"Final Game/Images/sprites/{sprite_choice}L2.png"), 
                pygame.image.load(f"Final Game/Images/sprites/{sprite_choice}L3.png")]
    sprite_r = [pygame.image.load(f"Final Game/Images/sprites/{sprite_choice}R1.png"), 
                pygame.image.load(f"Final Game/Images/sprites/{sprite_choice}R2.png"), 
                pygame.image.load(f"Final Game/Images/sprites/{sprite_choice}R3.png")]
    sprite_u = [pygame.image.load(f"Final Game/Images/sprites/{sprite_choice}U1.png"), 
                pygame.image.load(f"Final Game/Images/sprites/{sprite_choice}U2.png"), 
                pygame.image.load(f"Final Game/Images/sprites/{sprite_choice}U3.png")]
    
    portal_right_image = pygame.image.load("Final Game\Images\portalR.png")
    portal_left_image = pygame.image.load("Final Game\Images\portalL.png")

    #image, x, y
    portal_image_list = [[portal_left_image, 0, 0], [portal_right_image, HEIGHT - portal_right_image.get_width(), 600]]
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
                    x = portal_image_list[i + 1][1]
                    y = portal_image_list[i + 1][2]

        return x, y

    run = True
    #Variables for sprite position
    sprite_pos_x = 0
    sprite_pos_y = 610

    sprite_direction = "right"

    #list of coordinates for walls
    #x, y, width, height
    boundary_coordinate_list = [[600, 600, 100, 5], [600, 600, 5, 100], [0, 600, 500, 5],
                                [100, 0, 5, 500], [200, 100, 400, 5], [600, 100, 5, 400],
                                [500, 500, 105, 5], [500, 500, 5, 105], [100, 500, 300, 5],
                                [400, 400, 5, 105], [400, 400, 105, 5], [500, 200, 5, 200],
                                [400, 200, 5, 100], [300, 300, 105, 5], [300, 300, 5, 200],
                                [300, 100, 5, 100], [200, 200, 105, 5], [200, 200, 5, 200]]
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

        egg = window.blit(egg_image, (611, 610))
        # print(pygame.mouse.get_pos())
        keyPressed = pygame.key.get_pressed()

        if (sprite_num // 15) == len(sprite_l):
            sprite_num = 0

        #Choose sprite direction and then choose image
        if sprite_direction == 'left' or sprite_direction == 'down':
            image_current = sprite_l[sprite_num // 15]

        elif sprite_direction == 'right':
            image_current = sprite_r[sprite_num // 15]

        elif sprite_direction == 'up':
            image_current = sprite_u[sprite_num // 15]

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

        time_passed = pygame.time.get_ticks() - time_start
        stopwatch = TIMER_FONT.render(str(time_passed / 1000), True, (0,0,0))
        window.blit(stopwatch, (0, 0))

        #Check if egg has been hit
        if egg.colliderect(sprite_current):
            #add passed time to scoreboard file
            current_folder = os.path.dirname(os.path.abspath(__file__))
            with open(os.path.join(current_folder, 'scoreboard2.txt'), "a") as myfile:
                myfile.write(f"\n{name}- Level 2: {time_passed/1000}")
            
            return 'win'

        #Call portals function
        sprite_pos_x, sprite_pos_y = portals(sprite_current, sprite_pos_x, sprite_pos_y)
        
        text = TIMER_FONT.render('Back', 5, (0,0,0))
        back_text = window.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT - 50))

        sprite_pos_x, sprite_pos_y = check_collide(sprite_current, image_current, sprite_pos_x, sprite_pos_y, sprite_direction)

        if pygame.mouse.get_pressed()[0]:
            if back_text.collidepoint(pygame.mouse.get_pos()):
                return 'menu'

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
