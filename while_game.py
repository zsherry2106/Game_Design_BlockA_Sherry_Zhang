#Sherry Zhang
#9/21/21

#Control main game
#instructions of the game

import random

answer = input("Do you want to play: ")

while "y" in answer.lower():
    print("Welcome, guess a number between 0 and 100, you have 10 chances")
    num = int(input("Give a number "))

    #try and except here
    while num < 10:
        print(num)
        num += 5
    
    answer = input("Do you want to play again: ")
