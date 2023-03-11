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
if a >= b and a >= c and a >= d:
    first = a
    if b >= c and b >= d:
        second = b
        if c >= d:
            third = c
            fourth = d
        else:
            third = d
            fourth = c
    elif c >= b and c >= d:
        second = c
        if b >= d:
            third = b
            fourth = d
        else:
            third = d
            fourth = b
    if d >= b and d >= c:
        second = d
        if b >= c:
            third = b
            fourth = c
        else:
            third = c
            fourth = b


if b >= a and b >= c and b >= d:
    first = b
    if a >= c and a >= d:
        second = a
        if c >= d:
            third = c
            fourth = d
        else:
            third = d
            fourth = c
    elif c >= a and c >= d:
        second = c
        if a >= d:
            third = a
            fourth = d
        else:
            third = d
            fourth = a
    if d >= a and d >= c:
        second = d
        if a >= c:
            third = a
            fourth = c
        else:
            third = c
            fourth = a

if c >= a and c >= b and c >= d:
    first = c
    if a >= b and a >= d:
        second = a
        if b >= d:
            third = b
            fourth = d
        else:
            third = d
            fourth = b
    elif b >= a and b >= d:
        second = b
        if a >= d:
            third = a
            fourth = d
        else:
            third = d
            fourth = a
    if d >= a and d >= b:
        second = d
        if a >= b:
            third = a
            fourth = b
        else:
            third = b
            fourth = a

if d >= a and d >= b and d >= c:
    first = d
    if a >= b and a >= c:
        second = a
        if b >= c:
            third = b
            fourth = c
        else:
            third = c
            fourth = b
    elif b >= a and b >= c:
        second = b
        if a >= c:
            third = a
            fourth = c
        else:
            third = c
            fourth = a
    if c >= a and c >= b:
        second = c
        if a >= b:
            third = a
            fourth = b
        else:
            third = b
            fourth = a

# Print the result
print(first - second == second - third == third - fourth)