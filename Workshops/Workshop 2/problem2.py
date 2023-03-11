# Matthew Prendergast
# 30th March, 2022 - Problem 2 (Workshop - Week 2)

# Store the user inputs into variables. Cast to a float.
hours = float(input("Number of hours worked per day: "))
days = float(input("Number of days worked in a week: "))
salary = float(input("Annual salary: "))

# Print the results.
print("Hourly wage = $", salary / (days * hours * 52), sep="")