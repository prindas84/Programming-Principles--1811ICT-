# Matthew Prendergast
# 1st April, 2022 - Problem 2 (Workshop - Week 3)

# Input the base price, weight and distance.
base = float(input("How much is the base price? "))
weight = float(input("What is the weight? "))
distance = float(input("What is the distance? "))

# Declare and initialise the discount and cost variables.
discount, cost = 0, 0

# Calculate the discount rate.
if distance >= 3000:
    discount = 0.5
elif distance >= 2000:
    discount = 0.35
elif distance >= 1000:
    discount = 0.20
elif distance >= 500:
    discount = 0.15
else:
    discount = 0

# Calculate the shipping cost.
cost = base * weight * distance * (1 - discount)

# Print the output.
print("The shipping cost is", cost)

