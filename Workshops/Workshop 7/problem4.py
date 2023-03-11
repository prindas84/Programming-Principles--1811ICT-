# Matthew Prendergast
# 7th May, 2022 - Problem 3 (Workshop - Week 7)

# Prompt user to input a file name.
file_name = input("File name: ")

# Open the file and read all lines into a list
fhand = open(file_name, mode = "r")

# Initialise the variables.
characters = 0
words = 0
lines = 0

for line in fhand:

    # Count the characters.
    for i in line:
        characters += 1
    
    # Count the words.
    reader = line.strip().split(" ")
    words += len(reader)

    # Count the lines.
    lines += 1

print("Characters:", characters)
print("Words:", words)
print("Lines:", lines)

fhand.close()