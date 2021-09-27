#Sherry Zhang
#9/23/21

#Word guessing game

#os clear doens't work for me
import os
os.system('clear')
print()

import random

fruits = ["strawberry", "pineapple", "grape", "apple", "kiwi"]
hints =  ["this fruit is a berry", "this fruit goes on pizza", "this fruit is green or purple", "this fruit is red or green", "this fruit is fuzzy"]

#print instructions for the game
print("This is a guessing game. Try to guess the fruit I'm thinking of. You have 10 chances")
playing = input("Do you want to play this game? ")
print()

while "y" in playing:
    random_num = random.randint(0, len(fruits))
    random_fruit = fruits[random_num]
    print(random_fruit)

    chances = 10
    running = 1

    while running:
        guess = input("Guess a fruit, type stop to end: ")

        if guess == "stop":
            running = 0
        
        else:
            if random_fruit.lower() == guess.lower():
                print("You win!")
                running = 0
            
            elif random_fruit.lower() != guess.lower() and chances != 1:
                print("Guess again!")
            
            chances -= 1

            if running == 1 and chances != 0:
                print("Chances left:", chances)
            
            elif chances == 0:
                print("You ran out of chances")
                running = 0
            
            if chances == 3:
                print("Here is a hint,")
                print(hints[random_num])
        
        print()
    
    playing = input("Play again? ")
