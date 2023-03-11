# Matthew Prendergast - QUIZ (Programming Principals) - Problem 1
# 7th April, 2022

# Input the values required for the program.

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))

# Declare the small, medium and large variables
first, second, third, fourth = 0, 0, 0, 0

# Determine which numbers are the first, second, third, fourth.
if a > b:
    first = a
    second = b
else:
    first = b
    second = a

if c > first:
    third = second
    second = first
    first = c
elif c > second:
    third = second
    second = c
else:
    third = c

if d > first:
    fourth = third
    third = second
    second = first
    first = d
elif d > second:
    fourth = third
    third = second
    second = d
elif d > third:
    fourth = third
    third = d
else:
    fourth = d

print(first, second, third, fourth)

# Print the result
print(first - second == second - third == third - fourth)