#Sherry Zhang
#9/9/21

#+ - * / %
#Check for even numbers

#% - creates remainder from division - called mod

# import os
# os.system('cls')

num = int(input("Enter a number: "))
check = num % 2

#put 2 equal signs to check/evaluate
if check == 0:
    print("The number is even")
else:
    print("The number is odd")
