from PyTest import *
##////////////////// PROBLEM STATEMENT ///////////////////////
## Write Python code which, given two integers a and b,     //
## prints the largest of the two but, if they are the same, //
## it just prints the value of b                            //
##   12 10 -> 12                                            //
##   2 10 -> 10                                             //
##   2 20 -> 20                                             //
##////////////////////////////////////////////////////////////

# Input the values
a = int(input())
b = int(input())

# If A = B - Print B
# Else - Print the largest of A and B.
if a == b:
    print(b)
elif a > b:
    print(a)
else:
    print(b)