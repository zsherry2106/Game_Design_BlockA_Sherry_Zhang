# Sherry Zhang
# 9/2/21
# Program to calculate average of 4 tests 

# Variables
test1 = 90
test2 = 87
test3 = 89
test4 = 93
sum_tests = test1 + test2 + test3 + test4

# Declare Averages
average = (sum_tests)/4

# Display Average
print("The average:")
print(average)

test5 = int(input("input the 5th test score: "))
sum_tests += test5
average = sum_tests/5

print("New average:")
print(average)

# inputName = "My name is Sherry"
# #type() tells what type of data type it is
# print(type(inputName))


for j in range(0, 4):
    print(j)
