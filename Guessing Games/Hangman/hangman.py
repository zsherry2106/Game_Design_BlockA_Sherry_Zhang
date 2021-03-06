#Sherry Zhang
#9/27/21

#Hangman game 

import os
from datetime import datetime
os.system('clear')

import random

animals = ["tiger", "lion", "elephant", "giraffe", "monkey", "toucan"]
fruits = ["strawberry", "grape", "apple", "kiwi", "pineapple", "watermelon"]
colors = ["blue", "green", "red", "orange", "yellow", "pink"]
char_list = [] #list used to store characters ex: _ or letters that are correct

this_folder = os.path.dirname(os.path.abspath(__file__))

#creates categories for player to choose from
def Menu():
    while 1:
        #Create a menu to play game within categories of words
        print("""
            Menu
        1. Animals
        2. Fruits
        3. Colors
        4. Scoreboard
        5. Exit
        """)

        selection = input("Which category would you like? ")

        if selection.isdigit() and int(selection) <= 5:
            return int(selection)
        else:
            print("Please enter a number between 1 and 4")

#Uses selection from menu to select word from proper list
def selectWord(selection):
    if selection == 1:
        word = random.choice(animals)
    elif selection == 2:
        word = random.choice(fruits)
    elif selection == 3:
        word = random.choice(colors)

    return word

name = input("What is your name: ")

playing_count = 0
high_score = []

choice = Menu() #choose which category from menu

while choice < 5 and playing_count < 3:
    if choice != 4:
        random_word = selectWord(choice)
        # print(random_word)
        score = 0
        playing_count += 1

        #create character lists with _ to display guesses
        char_list = ["_ "] * len(random_word)
        
        chances = len(random_word) + 3
        print(f"You have {chances} chances\n")

        str_char = "".join(char_list)

        print(str_char)

        #while the player hasn't won or still has chances, continue, use break
        while 1:
            guess = input("Guess a letter of the word, type stop to end: ")
            guess = guess.lower()
            print()

            if guess == "stop":
                break

            #make sure input is exactly one letter
            elif guess.isalpha() and len(guess) == 1:
                #check if guess is in random word
                if guess in random_word and guess not in char_list:
                    for i in range(len(random_word)):
                        if random_word[i] == guess:
                            char_list[i] = guess
                            str_char = "".join(char_list)
                            score += 3
                
                    #check if the player has won
                    if str_char == random_word:
                        print("You won!")
                        score += 5*chances
                        break
                
                #Subtract chance for repeat guesses
                else:
                    print("You already guessed that letter!")
                    chances -= 1

            #if input is not one letter 
            else:
                print("Please guess a letter")
                chances -= 1

            #break if there are no chances left
            if chances == 0:
                print("You ran out of guesses")
                break

            print("Chances left", chances)
            print(f"{str_char}\n")
        
        high_score.append(score)
        
        print("\nthe word was", random_word)
        print("your score was", score)
        char_list = []
    
    else:
        print("\nScoreboard:")
        with open(os.path.join(this_folder, 'hangman.txt'), "r") as myfile:
            print(myfile.read())
    
    choice = Menu()

#If player exits at the beginning, do not run this code
if len(high_score) != 0:
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    #adds highscore to txt file
    with open(os.path.join(this_folder, 'hangman.txt'), "a") as myfile:
        myfile.write(f"\n{name} \tHighest score:\t {dt_string} {max(high_score)}")
