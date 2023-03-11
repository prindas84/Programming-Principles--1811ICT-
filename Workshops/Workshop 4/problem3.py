# Matthew Prendergast
# 19th April, 2022 - Problem 3 (Workshop - Week 4)

# Retrieve the user input.
number = int(input("Enter a positive number: "))

# Initilise the variable for the row count and number of spaces and crosses are required per row.
rows = 2 * number - 1
space, cross = 0, 0

# Build the top half of the diamond.
for i in range(1, rows + 1, 2):
    cross = i
    space = (rows - cross) // 2
    print(" " * space, "x" * cross, " " * space, sep="")

# Build the bottom half of the diamond.
for j in range(rows - 2, -1, -2):
    cross = j
    space = (rows - cross) // 2
    print(" " * space, "x" * cross, " " * space, sep="")




