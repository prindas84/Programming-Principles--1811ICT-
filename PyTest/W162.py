from PyTest import *
##//////////// PROBLEM STATEMENT //////////////////
## Given an int n, print the absolute difference //
## between n and 21, except print double the     //
## absolute difference if n is over 21.          //
##   19 -> 2                                     //
##   10 -> 11                                    //
##   21 -> 0                                     //
##/////////////////////////////////////////////////

# Input the value
a = int(input())

# If N > 21 - Print double the value. Else - Print absolute value
if a > 21:
    print(abs((a - 21) * 2))
else:
    print(abs(21 - a))