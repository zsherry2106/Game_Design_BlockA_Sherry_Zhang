#Sherry Zhang
#9/15/21

#Number Guessing game

#os clear doesn't work for me
import os
os.system('cls')

import random

random_num = random.randint(0, 100)

# input_num = input("Guess a number between 0 to 10: ")
running = 1
check = False
chances = 10

print(random_num)

print("Guess a number between 0 to 100, you have 10 chances")
while running:
    print()
    input_num = input("Guess a number between 0 to 100, type stop to end: ")

    if input_num == "stop":
        running = 0

    try:
        int(input_num)
        check = True

    except ValueError:
        if input_num != "stop":
            print("Input was not a number")

    if check == True:
        input_num = int(input_num)
        
        if 0 < input_num < 100:
            if abs(input_num - random_num) > 25:
                if input_num < random_num:
                    print("Number is too small!")
                
                elif input_num > random_num:
                    print("Number is too big!")
            elif abs(input_num - random_num) > 25 and input_num != random_num:
                print("Getting close")
            
            if input_num == random_num:
                print()
                print("You guessed the number!")
                play_again = input("Play again? Type Y if yes, type anything else if no ")
                play_again = play_again.lower()
                
                if play_again == "y":
                    chances = 11
                    input_num = False
                    random_num = random.randint(0, 100)
                else:
                    running = 0
        
        elif 100 < input_num or input_num < 0:
            print("Number was not between 0 and 100")
        
    chances -=1

    if chances == 0:# and running == 1:
        print(running)
        print()
        print("You lost! The number was", random_num)
        play_again = input("Play again? Type Y if yes, type anything else if no ")
        play_again = play_again.lower()
        
        if play_again == "y":
            random_num = random.randint(0, 100)
        else:
            running = 0
    elif running == 1 and input_num != False:
        print("Chances left:", chances)

print()
