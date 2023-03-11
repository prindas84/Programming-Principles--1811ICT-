from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////
## Given a non-empty string and an int N, print the string made starting //
## with char 0, and then every Nth char of the string. So if N is 3, use //
## char 0, 3, 6,. .. and so on. N is 1 or more.                          //
##   "Miracle", 2 -> "Mrce"                                              //
##   "abcdefg", 2 -> "aceg"                                              //
##   "abcdefg", 3 -> "adg"                                               //
##/////////////////////////////////////////////////////////////////////////

# Input the variables from the test file.
str = input()
increment = int(input())

# Loop over the string and print the required letters.
for x in range(0, len(str), increment):
    print(str[x], end = '')