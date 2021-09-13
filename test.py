#Sherry Zhang
#9/13/21

#Sherry's test page


#os clear does not work for me
import os
os.system('cls')

userInput = input("Type something ")

try:
    int(userInput)
    check = True
#checks if there is a error, goes to except if there is
except ValueError:
    check = False


if check:
    print("Input is an integer")
else:
    print("Length of input:", len(userInput))
    
    for i in userInput:
        print(i)
