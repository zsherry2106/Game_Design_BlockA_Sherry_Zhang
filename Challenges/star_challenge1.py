#Sherry Zhang
#9/7/21

#How to use for looping

stars = int(input("Enter number of stars: "))
stars2 = stars
line = stars
space = 0

for i in range(line):
    for j in range(space):
        # print(space)
        print("  ", end = " ")
    space += 1
    for counter in range(stars):
        print("* ", end=" ")
        # print(counter + 1, end=" ")
    
    print()
    stars -=1

#print empty line to return
print()
print("Thank You")


# stars = int(input("Enter number of stars: "))

# for counter in range(stars, 0, -1):
#     print("* "*counter)



