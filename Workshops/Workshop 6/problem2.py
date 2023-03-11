# Matthew Prendergast
# 2nd May, 2022 - Problem 2 (Workshop - Week 6)

# Prompt user to input a a list of numbers.
input_one = input("List 1: ")
input_two = input("List 2: ")

# Convert the input to a list.
list_one = input_one.split(" ")
list_two = input_two.split(" ")

# Count the first and last digit in each list.
if len(list_one) > 1:
    count_one = int(list_one[0]) + int(list_one[-1])
else:
    count_one = int(list_one[0])
if len(list_two) > 1:
    count_two = int(list_two[0]) + int(list_two[-1])
else:
    count_two = int(list_two[0])

# Print the output.
if count_one > count_two:
    print("Output:", count_one)
elif count_two > count_one:
    print("Output:", count_two)
else:
    print("Output: Same")


