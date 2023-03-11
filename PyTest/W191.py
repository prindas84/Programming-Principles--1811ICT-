from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given a string and an int n, print a string made of the first n           //
## characters of the string, followed by the  first n-1 characters of the    //
## string, and so on. You may assume that n is between 0 and the length of   //
## the string, inclusive (i.e. n >= 0 and n <= str.length()).                //
##   "Chocolate", 4 -> "ChocChoChC"                                          //
##   "Chocolate", 3 -> "ChoChC"                                              //
##   "Ice Cream", 2 -> "IcI"                                                 //
##/////////////////////////////////////////////////////////////////////////////

str = input()
n = int(input())

while n > 0:
    for i in range(n):
        print(str[i], end="")
    n -= 1
