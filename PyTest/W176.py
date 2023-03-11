import math
from PyTest import *
##///////////// PROBLEM STATEMENT //////////////
## Write a program that calculates and prints //
## a value according to the given formula:    //
##   Q = Square root of [(2 * C * D)/H]       // 
## Following are the fixed values of C and H: //
##   C is 50. H is 30.                        //
##   D is the value read by your program      //
##/////////////////////////////////////////////

# Input the value

d = int(input())

print(int(math.sqrt((2 * 50 * d) / 30)))