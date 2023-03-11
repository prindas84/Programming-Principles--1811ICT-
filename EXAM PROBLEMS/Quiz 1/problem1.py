# Matthew Prendergast - QUIZ (Programming Principals) - Problem 1
# 7th April, 2022

# Input the values required for the program.
large = float(input("Radius of the large circle: "))
small = float(input("Radius of the small circle: "))

# Calculate the radius of each circle
largeRad = 3.14 * large**2
smallRad = 3.14 * small**2

# Print the result
print("Difference between their areas: ", largeRad - smallRad)