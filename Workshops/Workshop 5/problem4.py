from math import ceil

# Matthew Prendergast
# 22nd April, 2022 - Problem 4 (Workshop - Week 5)

# Retrieve the user input.
dimention_one = float(input("Enter room dimension 1 (m): "))
dimention_two = float(input("Enter room dimension 2 (m): "))

while dimention_one != 0 and dimention_two != 0:

    # Initialise the variables.
    length, width, used_length, used_width = 0, 0, 0, 0

    # Check which dimension is the length and width.
    if dimention_one > dimention_two:
        length = dimention_one
        width = dimention_two
    else:
        length = dimention_two
        width = dimention_one

    # Print the length and the width of the room.
    print("Length of room = {:.3f} m".format(length))
    print("Width of room = {:.3f} m".format(width))

    # Calculate the useage for the length of the room.
    temp_width = width
    while temp_width > 0:
        used_length += length
        temp_width -= 3.66

    # Calculate the useage for the width of the room.
    temp_length = length
    while temp_length > 0:
        used_width += width
        temp_length -= 3.66

    # Print the length and width required.
    print("Total carpet length required in lengthways manner = {} m".format(ceil(used_length)))
    print("Total carpet length required in widthways manner =  {} m".format(ceil(used_width)))
    print()

    # Prompt the user for new dimensions.
    dimention_one = float(input("Enter room dimension 1 (m): "))
    dimention_two = float(input("Enter room dimension 2 (m): "))
