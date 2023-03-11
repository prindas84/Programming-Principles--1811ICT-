# Matthew Prendergast
# 19th April, 2022 - Problem 2 (Workshop - Week 4)

# Retrieve the user input.
number = int(input("Enter a positive number: "))

# Print value if the number is 0.
if number == 0:
    print(0)

# Print value if the number is 1.
elif number == 1:
    print(0, 1)

# Print value for all other number inputs, formatted as required.
else:
    first = 0
    second = 1
    count = 2
    print(first, second, end=" ")
    for i in range(2, number):
        print(first + second, end=" ")
        temp_first = first
        temp_second = second
        first = second
        second = temp_first + temp_second
        count += 1
        if count == 4:
            print("")
            count = 0

