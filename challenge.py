#Sherry Zhang
#9/7/21

#How to use for looping

stars = int(input("Enter number of stars: "))
stars2 = stars
line = stars
space = 0

for i in range(line):
    for counter in range(stars):
        print("* ", end=" ")
    stars -=1

    for j in range(space):
        print("  ", end = " ")
    space += 2
    
    for counter in range(stars2):
        print("* ", end=" ")
        # print(counter + 1, end=" ")
    
    print()
    stars2 -=1

#print empty line to return
print()
print("Thank You")


# stars = int(input("Enter number of stars: "))

# for counter in range(stars, 0, -1):
#     print("* "*counter)
