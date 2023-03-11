from PyTest import *
##//////////////// PROBLEM STATEMENT //////////////////
## Given a string, print a "rotated left 2" version  //
## where the first 2 chars are moved to the end. The //
## string length will be at least 2.                 //
##   "Hello" -> "lloHe"                              //
##   "Python" -> "thonPy"                            //
##   "Hi" -> "Hi"                                    //
##/////////////////////////////////////////////////////

str = input()

first = str[0] + str[1]

for i in range(2, len(str)):
    print(str[i], end="")
print(first)