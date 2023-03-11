# Matthew Prendergast
# 30th March, 2022 - Problem 3 (Workshop - Week 2)

# Set the constant variables for the rooms size and class size.
CLASS_SIZE = 25
BIG_HALL = 45
SMALL_HALL = 22

# Store the user inputs into variables. Cast to a int.
big_available = int(input("How many big exam halls? "))
small_available = int(input("How many small exam halls? "))

# Print the results.
print("Number of classes = ", (big_available * BIG_HALL + small_available * SMALL_HALL) // CLASS_SIZE)
