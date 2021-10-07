#Sherry Zhang
#9/27/21

#Hangman game 

import os
os.system('clear')

import random

animals = ["tiger", "lion", "elephant", "giraffe", "monkey", "toucan", "bear"]
fruits = ["strawberry", "grape", "apple"]
colors = ["blue", "green", "red", "orange", "yellow"]
char_list = [] #list used to store characters ex: _ or letters that are correct

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
            selection = int(selection)
            if selection <= 4:
                return selection
            else:
                print("Please enter a number between 1 and 4")
        
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

name = input("What is your name: ")

playing_count = 0
high_score = []

choice = Menu() #choose which category from menu
while choice != 4 and playing_count < 3:
    random_word = selectWord(choice)
    print(random_word)
    score = 0
    playing_count += 1

    #create character lists with _ to display guesses
    char_list = ["_ "] * len(random_word)
    
    chances = len(random_word) + 3
    print(f"You have {chances} chances")
    print()

    str_char = "".join(char_list)

    print(str_char)

    #while the player hasn't won or still has chances
    while 1:
        guess = input("Guess a letter of the word, type stop to end: ")
        guess = guess.lower()
        print()

        if guess == "stop":
            break

        elif guess.isalpha() and len(guess) == 1:
            #check if guess is in random word
            if guess in random_word and guess not in char_list:
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
    
    #Give user 1 point for every correct guess
    for i in char_list:
        if i.isalpha():
            score += 1
    
    score += chances
    high_score.append(score)
    
    print("the word was", random_word)
    print("your score was", score)
    char_list = []

    if playing_count != 3:
        choice = Menu()

print(high_score)
print(max(high_score))

score_file = open("hangman.txt", "a")  # append mode
score_file.write(f"{max(high_score)}")
score_file.close()
