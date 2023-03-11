# Matthew Prendergast
# 7th May, 2022 - Problem 2 (Workshop - Week 7)

# Prompt user to input a file name.
file_name = input("File name: ")

# Open the file and read all lines into a list
fhand = open(file_name, mode = "r")
ls = fhand.readlines()

# Print the result.
print("Output:")
print(ls[0], ls[1], ls[-2], ls[-1], sep="")

fhand.close()