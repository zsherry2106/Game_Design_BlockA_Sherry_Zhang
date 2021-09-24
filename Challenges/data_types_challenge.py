#Sherry Zhang
#9/10/21

#Data Types Challenge

#os clear does not work for me
import os
os.system('cls')

#create variables with dfferent data types and print data type
# variable1 = "hello"
# variable2 = True
# variable3 = 19
# variable4 = 20.1

# print(variable1, "data type:", type(variable1))
# print(variable2, "data type:", type(variable2))
# print(variable3, "data type:", type(variable3))
# print(variable4, "data type:", type(variable4))

input1 = input("Enter something ")
check = "str"

try:
    int(input1)
    check = "int"
except ValueError:
    try:
        float(input1)
        check = "float"
    except ValueError:
        pass

if check == "int":
    print("input is an integer")

elif check == "float":
    print("input is a float")

else:
    print("input is a string")

print()
print()



#Calculate addition, subtraction, multiplication, and division of 2 variables of same type 
#Print the result 
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

try:
    int(num1)
    int(num2)
    check = True
except ValueError:
    check = False

if check == True:
    num1 = int(num1)
    num2 = int(num2)
    add = num1 + num2
    sub = num1 - num2
    mult = num1 * num2
    div = num1 / num2

    print("+:", add, ", -:", sub, ", *:", mult, ", /:", div)

else:
    print("input were not numbers")

print()
print()



#Calculate the modulus of two of the variables
#Modulus is a operator that finds the remainder after division

mod1 = int(input("Enter a number: "))
mod2 = int(input("Enter another number: "))

try:
    int(mod1)
    int(mod2)
    check = True
except ValueError:
    check = False

if check == True:
    mod1 = int(mod1)
    mod2 = int(mod2)
    mod = mod1 % mod2

    print("% (remainder):", mod)

    
    

else:
    print("input were not numbers")
