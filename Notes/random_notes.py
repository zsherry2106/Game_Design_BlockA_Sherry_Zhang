
import random
import os

os.system('cls')

random.seed(20)

#used to test random
for i in range(10):
    rand1 = random.randint(3, 5)

    random2 = random.random()
    random2 *= 100
    #print(int(random2))

fruits = ["apple", "banana", "berry", "grape"]
my_fruit = random.choice(fruits)
print(my_fruit)
