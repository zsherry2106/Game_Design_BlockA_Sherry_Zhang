#Sherry Zhang
#9/25/21

#Reverse str using funtion

import os
os.system('clear')

def reverse_str(str1):
    return str1[:: -1]

str_input = input("Enter a str: ")
new_str = reverse_str(str_input)
print(new_str)
