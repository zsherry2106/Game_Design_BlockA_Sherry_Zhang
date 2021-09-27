#Sherry Zhang
#9/25/21

#Reverse str using funtion

def reverse_str(str1):
    len_str = len(str1)
    return str1[len_str :: -1]

str_input = input("Enter a str: ")
new_str = reverse_str(str_input)
print(new_str)
