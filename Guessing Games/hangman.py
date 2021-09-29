#Sherry Zhang
#9/27/21

#Hangman game 

import os
os.system('clear')

import random

animals = ["tiger", "lion", "elephant", "giraffe"]
char_list = []

chance_check = False

print("In this game, you will guess letters in an animal's name one by one. You will only lose a chance if you guess incorrectly.")
playing = input("Do you want to play this game? ")

#while the player wants to play
while "y" in playing:
    random_anim = random.choice(animals)
    # print(random_anim)
    running = 1

    #create character lists with _ to display guesses
    for i in random_anim:
        char_list.append("_ ")
    
    chances = len(random_anim) + 3
    print(f"You have {chances} chances")
    print()

    str_char = "".join(char_list)

    print(str_char)

    #while the player hasn't won or still has chances
    while running and chances > 0:
        guess = input("Guess a letter of an animal, type stop to end: ")
        print()

        if guess.lower() != "stop":
            #if input is an integer, subtract a guess and do not continue
            try:
                int(guess)
                print("Please guess a letter")
                chances -= 1

            except ValueError:
                #make sure guess is 1 letter, not multiple
                if len(guess) < 2:

                    #check if guess is in random word
                    for i in range(len(random_anim)):
                        if random_anim[i] == guess.lower():
                            char_list[i] = f"{guess.lower()}"
                            chance_check = True
                            str_char = "".join(char_list)
                    
                    #create message that they guessed incorrectly
                    if chance_check == False:
                        chances -= 1
                        print("incorrect guess")

                    #check if the player has won
                    if str_char == random_anim:
                        print("You won!")
                        running = 0
                    
                    #check chances to print why the player has lost
                    if chances == 0:
                        print("You have run out of chances")

                    #print chances left
                    elif running == 1:
                        print("Chances left", chances)

                #subtract guess if player guesses multiple char
                else:
                    print("Please guess a letter")
                    chances -= 1

                print(str_char)
        else:
            running = 0
        
        chance_check = False
        
        print()
    
    print("the word was", random_anim)
    playing = input("Do you want to play again? ")
    char_list = []
