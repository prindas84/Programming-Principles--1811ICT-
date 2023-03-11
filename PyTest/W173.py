from PyTest import *
##//////////// PROBLEM STATEMENT ///////////////
## Write a program which takes a number n and //
## adds up the numbers in the range 0..n      //
##    3 -> 6                                  //
##   10 -> 55                                 //
##   20 -> 210                                //
##//////////////////////////////////////////////

# Input the value
x = int(input())

# Calculate the count
count = 0

for y in range(x + 1):
    count += y

# Print the count
print(count)