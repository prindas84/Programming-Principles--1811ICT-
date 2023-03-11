# Matthew Prendergast
# 24th May, 2022 - Problem 3 (Workshop - Week 9)

from math import sqrt

# Prompt the user to input the grid references.
x = input("Enter trip map references: ")
references = x.split()

# Set the global distance for each grid space and initialise the total distance to 0.
GRID = 500
distance = 0

# Check the list for bad references.
for j in range(len(references)):
    if not references[j][0].isupper():
        print("Bad reference:", references[j])
        exit()
    elif not references[j][1:].isdigit():
        print("Bad reference:", references[j])
        exit()

# Calculate the distance between each position and increment the distance count.
for i in range(len(references) - 1):
    y1 = ord(references[i][0])
    x1 = int(references[i][1:])
    y2 = ord(references[i + 1][0])
    x2 = int(references[i + 1][1:])

    distance += sqrt(abs(y1 - y2) ** 2 + abs(x1 - x2) ** 2) * GRID

# Print the result.
print(f"Total distance = {distance / 1000:.1f} km")
