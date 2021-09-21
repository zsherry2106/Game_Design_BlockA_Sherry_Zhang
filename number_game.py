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

# print(random_num)

while running and chances != 0:
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

        if input_num == random_num:
            print("You guessed the number!")
            play_again = input("Play again? Type Y or N ")
            play_again = play_again.lower()
            
            if play_again == "y":
                random_num = random.randint(0, 100)
            elif play_again == "n":
                running = 0
        
        if abs(input_num - random_num) > 25:
            if input_num < random_num:
                print("Number is too small!")
            
            elif input_num > random_num:
                print("Number is too big!")
        else:
            print("Getting close")
        
    chances -=1
    print("Chances left:", chances)

print()
