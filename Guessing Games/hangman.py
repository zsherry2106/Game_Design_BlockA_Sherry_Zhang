#Sherry Zhang
#9/27/21

#Hangman game 

import os
os.system('clear')

import random

animals = ["tiger", "lion", "elephant", "giraffe"]
char_list = []

print("In this game, you will guess letters in an animal's name one by one. You will only lose a chance if you guess incorrectly.")
playing = input("Do you want to play this game? ")

#while the player wants to play
while "y" in playing:
    random_anim = random.choice(animals)
    # print(random_anim)

    #create character lists with _ to display guesses
    char_list = ["_ "] * len(random_anim)
    
    chances = len(random_anim) + 3
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
            if guess in random_anim:
                for i in range(len(random_anim)):
                    if random_anim[i] == guess:
                        char_list[i] = guess
                        str_char = "".join(char_list)
            
                #check if the player has won
                if str_char == random_anim:
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
    
    print("the word was", random_anim)
    playing = input("Do you want to play again? ")
    char_list = []
