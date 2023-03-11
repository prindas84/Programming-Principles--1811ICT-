# Matthew Prendergast
# 19th April, 2022 - Problem 4 (Workshop - Week 4)

# Retrieve the user input.
number = input("Enter a positive number: ")

# Initialise the variables to use.
length = len(number)
count = 0

# Create the loop to test the string and print the result.
for i in range(length):
    if number[i] != number[length - (i + 1)]:
        count +=1
if count == 0:
    print(number, "is a palindrome")
else:
    print(number, "is not a palindrome")

