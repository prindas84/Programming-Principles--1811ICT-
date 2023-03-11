# Matthew Prendergast
# 22nd April, 2022 - Problem 1 (Workshop - Week 5)

# Retrieve the user input.
sentance = input("Enter a string: ")

# Initialise the longest string count, and set the longest sentance to the first sentance inputted.
long_count = 0
long_string = sentance

# While the first letter is not A, compare the string to the current longest and reprompt the user for a new string.
while sentance[0] != "A":
    length = len(sentance)
    if length > long_count:
        long_count = length
        long_string = sentance
    sentance = input("Enter a string: ")

# Print the result.
print(f"Longest was: '{long_string}'")
