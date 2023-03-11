# Matthew Prendergast
# 30th March, 2022 - Problem 3 (Workshop - Week 2)

# Input the three integers.
a = int(input("Integer 1? "))
b = int(input("Integer 2? "))
c = int(input("Integer 3? "))

# Print the integers in decending order using nested loops.
if a >= b and a >= c:
    print(a, end=" ")
    if b >= c:
        print(b, c)
    else:
        print(c, b)
elif b >= a and b >= c:
    print(b, end=" ")
    if a >= c:
        print(a, c)
    else:
        print(c, a)
else:
    print(c, end=" ")
    if a >= b:
        print(a, b)
    else:
        print(b, a)