from PyTest import *
##///////////// PROBLEM STATEMENT /////////////////////
## Read 3 integers and print them in ascending order //
##   1 3 2 -> 1 2 3                                  //
##   3 1 2 -> 1 2 3                                  //
##   8 5 2 -> 2 5 8                                  //
##/////////////////////////////////////////////////////

# Input the values
a = int(input())
b = int(input())
c = int(input())

# Print in ascending order.
if a <= b and a <= c:
    print(a, end=" ")
    if b <= c:
        print(b, c)
    else:
        print(c, b)
    
if b <= a and b <= c:
    print(b, end=" ")
    if a <= c:
        print(a, c)
    else:
        print(c, a)

if c <= a and c <= b:
    print(c, end=" ")
    if a <= b:
        print(a, b)
    else:
        print(b, a)