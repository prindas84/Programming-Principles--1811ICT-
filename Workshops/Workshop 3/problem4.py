# Matthew Prendergast
# 30th March, 2022 - Problem 4 (Workshop - Week 2)

# Input the values
hours = int(input("How many hours were worked? "))
cars_sold = int(input("Total number of cars sold for the week? "))

# Declare and initialise the variables to use.
RATE = 36.25
base_salary, overtime, bonus = 0, 0, 0

# Calculate the car sales bonus.
if cars_sold > 5:
    bonus = (cars_sold - 5) * 200

# Calculate the salary based on the number of hours inputted.
if hours > 37:
    base_salary = 37 * RATE
    overtime = (hours - 37) * RATE * 1.5
else:
    base_salary = hours * RATE

# Print the salary.
print("The salary is ", base_salary + overtime + bonus)
