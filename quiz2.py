# Sherry Zhang
# 10/5/21

# Quiz number 2

import os
os.system('clear')

#Question number 1:
print(len('Hello World!'))

# Quetion number 2:
strString = 'Study.com is a wonderful resource.'
print(strString.find('great'))
print(strString.find('wonderful'))
print(strString.find('.'))
 
#Question number 3:
strString = 'Study.com is a wonderful resource.'
print(strString[15:24])

#Question number 4:
str1 = "hello world."
print(str1[0])

#Question number 5:
strString = 'Study.com is a wonderful resource.'
print(strString[15:24].find('der') + len(strString))

#Question number 6:
var1 = 17
var2 = 4
result = var1 % var2
print(result)

#Question number 7:
print("\thello")

#Question number 8:
print("Hello\nworld")

#Question number 9:
str1 = "hello"
str2 = "world"
print(str1 + str2)

#Question number 10:
MyList = ['0', '1', '2', '3', '4', '6', '7', '8', '9', '10']
MyList.insert(5, '5')
print(MyList)
