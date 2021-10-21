#Sherry Zhang
#10/21/21

#Color Wheel challenge 

import os
os.system('clear')

primary = ['red', 'blue', 'yellow']
mix = {'orange': ['yellow', 'red'],
       'violet': ['red', 'blue'],
       'green': ['blue', 'yellow']}

color_input = 0
while color_input != 'stop':
    while 1:
        color_input = (input("Enter a color you want: ")).lower()

        if color_input.isdigit():
            print("Please enter a color")
        
        else:
            break

    if "-" in color_input:
        color = color_input.split("-")
        print(f"In order to make {color_input}, {color[0]} and {color[1]} must be mixed\n")

    elif color_input in primary:
        print(f"No colors need to be mixed to make {color_input}\n")

    elif color_input in mix.keys():
        color = mix.get(color_input)
        print(f"In order to make {color_input}, {color[0]} and {color[1]} must be mixed\n")

    else:
        color = "Not a color"
