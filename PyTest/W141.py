from PyTest import *
##////////////// PROBLEM STATEMENT ////////////////
## We'll say that a number is "teen" if it is in //
## the range 13..19 inclusive. Given 3 integer   //
## values, print True if 1 or more of them are   //
## teen.                                         //
##   13, 20, 10 -> True                          //
##   20, 19, 10 -> True                          //
##   20, 10, 13 -> True                          //
##/////////////////////////////////////////////////

# Input the values
a = int(input())
b = int(input())
c = int(input())

# Create the statement to print the result.
if 13<=a<=19 or 13<=b<=19 or 13<=c<=19:
    print("True")
else:
    print("False")
