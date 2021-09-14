#Sherry Zhang
#9/13/21

#Strings Homework

#os clear doesn't work for me
import os
os.system('cls')


print("Hello")
print()

#assign variables to strings
a = "Hello"

#use 3 quotes to distinguish lines
dif_lines = """Hello
Test"""
print("Use different 3 quotations to print different lines:")
print(dif_lines)
print()

#strings are arrays - access using brackets []
array = "Hello World"
print("String is array, access 2nd term:", array[1])

#loop through string to display each character individually
for i in array:
    print(i)

#find len by using len()
len_str = len(array)

#check if str is in main str or not in main str
check = "Hello world!"
print("Check if world is in str:", "world" in check)
print("Check if test is not in str:", "test" not in check)

print()
print()
print()


#slicing:
print("slicing:")

#doesn't include last number
slice_str = "Hello, world!"
print(slice_str[2:5])

print(slice_str[2:])
print(slice_str[:5])

#use negative numbers to start from end of
print(slice_str[-5:])

print()
print()
print()


#modifying:
print("modifying") 
modify = "hello, world!"

#upper changes all letters to uppercase, lower to lowercase
print(modify.upper())
print(modify.lower())

#strip - remove all spaces from beginning or end
modify2 = " hello, world!"
print(modify.strip())

#replace - first char - replacee, 2nd - replaced with
print(modify.replace("h", "j"))

#split - splits into list at inputed char, removes char inputed from list
print(modify.split(','))

print()
print()
print()


#concacting:
print("concacting")
concat1 = "hello"
concat2 = "world"

print(concat1 + concat2)
print(concat1 + " " + concat2)

print()
print()
print()


#formatting:
#places strings where {} are
print("formatting")
quantity = 3
itemno = 567
price = 49.95

order = "I want {0} of item number {1} for {2} dollars"
print(order.format(quantity, itemno, price))

print()
print()
print()


#escape characters:
#used to type characters like ""
print("John said, \"goodbye\"")
