#Sherry Zhang
#9/21/21

#Sherry Zhang
#9/15/21

#Number Guessing game

#os clear doesn't work for me
import os
os.system('cls')

import random

running = 1

playing = input("Do you want to play this game? Type yes or y ")

#While user wants to play the game
while "y" in playing:
    print("Guess a number between 0 to 100, you have 10 chances")
    random_num = random.randint(0, 100)
    print(random_num)
    check = False
    chances = 10

    #while user still has guesses and hasn't guessed the number
    while running:
        print()
        input_num = input("Guess a number between 0 to 100, type stop to end: ")
        #Stop code if user wants to  stop
        if input_num == "stop":
            running = 0

        #Try to convert to int
        try:
            int(input_num)
            check = True

        except ValueError:
            if input_num != "stop":
                print("Input was not a number")
                check = False

        #if value is int
        if check == True:
            input_num = int(input_num)
            
            #if number is between 0 and 100, continue
            if 0 < input_num < 100:

                #If number is not within 25 of the random number, give hints
                if abs(input_num - random_num) > 25:
                    #Give hints
                    if input_num < random_num:
                        print("Number is too small!")
                    
                    elif input_num > random_num:
                        print("Number is too big!")

                #If number is within 25 of random number, give no hints
                elif abs(input_num - random_num) > 25 and input_num != random_num:
                    print("Getting close")
                
                #If number is guessed, ask to play again
                if input_num == random_num:
                    print()
                    print("You guessed the number!")
                    running = 0
            
            elif 100 < input_num or input_num < 0:
                print("Number was not between 0 and 100")
            
        #Subtract chances every time
        chances -=1

        #If the player has no more chances:
        if chances == 0:
            print()
            print("You ran out of chances")
            running = 0
        
        #Print number of chances left
        elif running == 1 and input_num != False:
            print("Chances left:", chances)

    print()
    playing = input("Play again? Type yes or y ")

