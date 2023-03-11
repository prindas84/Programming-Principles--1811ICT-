from PyTest import *
##//////// PROBLEM STATEMENT ////////////
## Given 3 numbers, print the largest. //
##   3 2 1 -> 3                        //
##   1 2 3 -> 3                        //
##   3 3 3 -> 3                        //
##///////////////////////////////////////

# Input the values
a = int(input())
b = int(input())
c = int(input())

# Print the largest value
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)