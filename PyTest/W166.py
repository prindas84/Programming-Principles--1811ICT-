from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given three ints, a b c, print True if one of b or c is "close"           //
## (differing from a by at most 1), while the  other is "far", differing     //
## from both other values by 2 or more.                                      //
##                                                                           //
##   1 2 10 -> True                                                          //
##   1 2 3 -> False                                                          //
##   4 1 3 -> True                                                           //
##/////////////////////////////////////////////////////////////////////////////

# Input the values
a = int(input())
b = int(input())
c = int(input())

# Print the statement.
if abs(a - b) <= 1:
    if abs(a - c) >= 2 and abs(b - c) >= 2:
        print("True")
    else:
        print("False")
        
elif abs(a - c) <= 1:
    if abs(a - b) >= 2 and abs(b - c) >= 2:
        print("True")
    else:
        print("False")