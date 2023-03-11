from PyTest import *
##/////////////// PROBLEM STATEMENT ////////////////
## Given two temperatures, print True if one is   //
## less than 0 and the other is greater than 100. //
##   120, -1 -> True                              //
##   -1, 120 -> True                              //
##   2, 120 -> False                              //
##//////////////////////////////////////////////////

# Input the values
a = float(input())
b = float(input())

# If a is less than 0 and b is greater than 100 - PRINT TRUE.
if a < 0 and b > 100:
    print("True")

# If b is less than 0 and a is greater than 100 - PRINT TRUE.
elif b < 0 and a > 100:
    print("True")

# Else - PRINT FALSE
else:
    print("False")
