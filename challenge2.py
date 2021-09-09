
#Sherry Zhang
#9/9/21

#Find last, 2 last, and 3 last digits of a number

import os
os.system('cls')

num = int(input("Enter a number: "))

dig1 = num % 10
print("Last digit:", dig1)


if num < 10:
    print("Number is too short")
else:
    dig2 = num % 100
    print("2 Last digits:", dig2)


if num < 100:
    print("Number is too short")
else:
    dig3 = num % 1000
    print("3 Last digits:", dig3)
