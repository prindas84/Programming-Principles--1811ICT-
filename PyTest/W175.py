from PyTest import *
##///////////// PROBLEM STATEMENT ///////////////
## Write a program which will find all numbers //
## which are divisible by 7 but are not a      //
## multiple of 5, between 2000 and 2100        //
##///////////////////////////////////////////////

for x in range(2000, 2101):
    if x % 7 == 0 and x % 5 != 0:
        print(x)