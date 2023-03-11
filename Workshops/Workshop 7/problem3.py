# Matthew Prendergast
# 7th May, 2022 - Problem 3 (Workshop - Week 7)

# Prompt user to input a file name.
file_name = input("File name: ")

# Open the file and read all lines into a list
fhand = open(file_name, mode = "r")

# Initialise the line count.
count = 1

# Loop through all of the lines in the file.
for line in fhand:

    # Create a new list for each line of scores. Cast to integers. Find the average.
    scores = line.strip().split(" ")
    for i in range(len(scores)):
        scores[i] = int(scores[i])
    total = sum(scores) / len(scores)

    # Print the result. Increment the line count.
    print("The average of line", count, "is", total)
    count += 1

fhand.close()
    