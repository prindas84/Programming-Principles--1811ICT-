from inspect import formatargvalues
from PyTest import *
##///////////// PROBLEM STATEMENT //////////////
## Write a program that computes the value of //
## n+nn+nnn+nnnn with the single digit n      //
## input by the user.                         //
##//////////////////////////////////////////////

n = int(input())

one = n
two = n + one * 10
three = n + two * 10
four = n + three * 10

print(one + two + three + four)