from PyTest import *
##///////////////// PROBLEM STATEMENT ////////////////////
## Given an integer, print True if it is greater than   //
## zero and print False if it is not greater than zero. //
##   12 -> True                                         //
##   0  -> False                                        //
##   -8 -> False                                        //
##////////////////////////////////////////////////////////

# Input an integer
a = int(input())

# If is greater than 0 print True. Else print false.
if a > 0:
    print("True")
else:
    print("False")