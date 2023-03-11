from PyTest import *
##/////////// PROBLEM STATEMENT ///////////////
## Given 2 int values, print True if either  //
## of them is in the range 10..20 inclusive. //
##   12, 99 -> True                          //
##   21, 12 -> True                          //
##   8, 99 -> False                          //
##/////////////////////////////////////////////

# Input the values
a = int(input())
b = int(input())

# If either value in range 10-20 - PRINT TRUE
print(10<=a<=20 or 10<=b<=20)