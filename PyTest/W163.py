from PyTest import *
##///////////////////////// PROBLEM STATEMENT //////////////////////////
## Given three ints, a b c, one of them is small, one is medium and   //
## one is large. Print True if the three values are evenly spaced,    //
## so the difference between small and medium is the same as the      //
## difference between medium and large.                               //
##   2 4 6 -> True                                                    //
##   4 6 2 -> True                                                    //
##   4 6 3 -> False                                                   //
##//////////////////////////////////////////////////////////////////////

# Input the values
a = int(input())
b = int(input())
c = int(input())

# Declare the small, medium and large variables
small, medium, large = 0, 0, 0

# Determine which numbers are the small, medium and large.
if a >= b and a >= c:
    large = a
    if b >= c:
        medium = b
        small = c
    else:
        medium = c
        small = b
    
if b >= a and b >= c:
    large = b
    if a >= c:
        medium = a
        small = c
    else:
        medium = c
        small = a

if c >= a and c >= b:
    large = c
    if a >= b:
        medium = a
        small = b
    else:
        medium = b
        small = a

if medium - small == large - medium:
    print("True")
else:
    print("False")