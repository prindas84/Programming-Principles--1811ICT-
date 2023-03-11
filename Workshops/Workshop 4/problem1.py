# Matthew Prendergast
# 19th April, 2022 - Problem 1 (Workshop - Week 4)

# Retrieve the user input.
number = int(input("Enter a number: "))

# Declare a count variable.
count = 0

# Repeat the question until a user types 0.
while number != 0:
    if number > 0:
        count += 1
    number = int(input("Enter a number: "))

# Print the result.
print(f"{count} positive numbers were entered.")


