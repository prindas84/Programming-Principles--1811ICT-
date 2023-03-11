# Matthew Prendergast
# 2nd May, 2022 - Problem 1 (Workshop - Week 6)

# Prompt user to input a string.
str = input("Enter a string: ")

# Loop until an empty sting has been entered.
while len(str) > 0:

    # Convert the string to lowercase, split it into a list and sort it.
    str = str.lower()
    split_list = str.split(" ")
    split_list.sort(reverse=True)

    # Print the new sentence.
    print("Output: ", end="")
    for j in range(len(split_list)):
        print(split_list[j], end=" ")
    print() 

    # Prompt user to re-enter the string.
    str = input("Enter a string: ")