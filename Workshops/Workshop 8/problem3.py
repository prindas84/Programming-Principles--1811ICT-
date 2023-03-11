# Matthew Prendergast
# 17th May, 2022 - Problem 3 (Workshop - Week 8)

def num_check(num_list):
    """This function will calculate the difference between the first two numbers,
       then compare that to the difference between the other numbers in the array"""
    difference = num_list[0] - num_list[1]

    for j in range(1, len(num_list) - 1):
        if num_list[j] - num_list[j + 1] != difference:
            return False

    return True

# Prompt user to input a the file names.
file_read = input("File name: ")

# Open the file to read:
while True:
    try:
        f_read = open(file_read, mode = "r")
        break
    except:
        print("Error: File cannot be opened")
        file_read = input("File name: ")

# For each line in the text file
for line in f_read:

    # Read the line and convert it to a list. Convert the string elements to integers.
    num_list = line.split(" ")
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    
    # Print the list, and the return value of the function to compare the numbers.
    if line[-1] == "\n":
        print(f"[{line[:-1]}]", end=" ")
    else:
        print(f"[{line}]", end=" ")
    print(num_check(num_list))

# Close the file.
f_read.close()