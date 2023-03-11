from PyTest import *
##//////////////////////////// PROBLEM STATEMENT ///////////////////////////
## Given a number n, write while and for loops that add up the numbers in //
## the series 1,2,3,4,..., n-2, n-1, n and display the resultant sum. The //
## number n will be input by the user of the algorithm.                   //
##   10 -> 55 55                                                          //
##//////////////////////////////////////////////////////////////////////////

# Input the value.

x = int(input())

count = 0

# FOR LOOP
for y in range(x + 1):
    count += y

# Print the count
print(count)

count = 0
start = 0

# WHILE LOOP
while start <= x:
    count += start
    start += 1

# Print the count
print(count)



