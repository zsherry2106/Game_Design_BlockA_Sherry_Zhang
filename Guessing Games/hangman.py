#Sherry Zhang
#9/27/21

#Hangman game 

import os
os.system('clear')

import random

animals = ["tiger", "lion", "elephant", "giraffe", "monkey", "toucan", "bear", "panda"]
fruits = ["strawberry", "grape", "apple"]
colors = ["blue", "green", "red", "orange", "yellow"]
char_list = []

def Menu():
    while 1:
        #Create a menu to play game within categories of words
        print("""
            Menu
        1. Animals
        2. Fruits
        3. Colors
        4. Exit
        """)

        selection = input("Which category would you like? ")

        if not selection.isalpha():
            return int(selection)
        
        else:
            print("Please enter a number")

def selectWord(selection):
    # print(type(selection))
    if selection == 1:
        word = random.choice(animals)

    elif selection == 2:
        word = random.choice(fruits)
    
    elif selection == 3:
        word = random.choice(colors)

    return word

choice = Menu()
while choice != 4:
    random_word = selectWord(choice)
    print(random_word)

    #create character lists with _ to display guesses
    char_list = ["_ "] * len(random_word)
    
    chances = len(random_word) + 3
    print(f"You have {chances} chances")
    print()

    str_char = "".join(char_list)

    print(str_char)

    #while the player hasn't won or still has chances
    while 1:
        guess = input("Guess a letter of an animal, type stop to end: ")
        guess = guess.lower()
        print()

        if guess == "stop":
            break

        elif guess.isalpha() and len(guess) == 1:
            #check if guess is in random word
            if guess in random_word:
                for i in range(len(random_word)):
                    if random_word[i] == guess:
                        char_list[i] = guess
                        str_char = "".join(char_list)
            
                #check if the player has won
                if str_char == random_word:
                    print("You won!")
                    break
            
            else:
                chances -= 1
                print("incorrect guess")
                if chances == 0:
                    print("Ran out of chances")
                    break 

        else:
            chances -= 1
            print("Please guess a letter")
            if chances == 0:
                print("You ran out of guesses")
                break

        print("Chances left", chances)
        print(str_char)
        
        print()
    
    print("the word was", random_word)
    choice = Menu()
    char_list = []
