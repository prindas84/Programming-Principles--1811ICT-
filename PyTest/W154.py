from PyTest import *
##////////////////////// PROBLEM STATEMENT //////////////////////////
## You have a blue lottery ticket, with ints a, b, and c on it.    //
## This makes three pairs, which we'll call ab, bc and ac.         //
## Consider the sum of the numbers in each pair. If any pair sums  //
## to exactly 10, the result is 10. Otherwise if the ab sum is     //
## exactly 10 more than either bc or ac sums, the result is 5.     //
## Otherwise the result is 0.                                      //
##   9, 1, 0 -> 10                                                 //
##   9, 2, 0 -> 0                                                  //
##   6, 1, 4 -> 10                                                 //
##///////////////////////////////////////////////////////////////////

# Input the values
a = int(input())
b = int(input())
c = int(input())

# If ANY pair totals to 10 - PRINT 10
# If the pair AB = BC + 10, or AC + 10 - PRINT 5
# Else - Print 0
if (a + b == 10) or (b + c == 10) or (a + c == 10):
    print(10)
elif (a + b == b + c + 10) or (a + b == a + c + 10):
    print(5)
else:
    print(0)




