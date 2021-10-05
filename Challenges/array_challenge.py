#Sherry Zhang
#10/5/21

#Array Challenge:
#Ask user for length of array, randomize array with numbers, print the array backwards

import os, random
os.system('clear')

array = []

while 1:
    len_array = input("Enter a number for the length of the array: ")
    try:
        len_array = int(len_array)
        break
        
    except ValueError:
        print("Please enter a number")

while 1:
    num_reverse = input("Enter a number where you want the array to be reversed: ")
    try:
        num_reverse = int(num_reverse)
        break
        
    except ValueError:
        print("Please enter a number")

for i in range(len_array):
    array.append(i+1)

print("Original array:")
print(array)
print()

random.shuffle(array)
print("Shuffled array:")
print(array)
print()

array = array[:: -num_reverse]
print("Shuffled, reversed array")
print(array)
print()
