# Matthew Prendergast - QUIZ (Programming Principals) - Problem 1
# 7th April, 2022

# Input the values required for the program.
points = float(input("Status credits: "))

# Create the if statement to print the results.
if points < 300:
    print("Your membership tier is: Bronze")
    print("Status credits needed to reach the next tier: ", int(300 - points))
elif 300 <= points < 700:
    print("Your membership tier is: Silver")
    print("Status credits needed to reach the next tier: ", int(700 - points))
elif 700 <= points < 1400:
    print("Your membership tier is: Gold")
    print("Status credits needed to reach the next tier: ", int(1400 - points))
elif 1400 <= points < 3600:
    print("Your membership tier is: Platinum")
    print("Status credits needed to reach the next tier: ", int(3600 - points))
else:
    print("Your membership tier is: Platinum One")
    print("Status credits needed to reach the next tier: 0")

