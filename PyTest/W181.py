from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given a string, print a string length 2 made of its first 2 chars. If the //
## string length is less than 2, use  '@' for the missing chars.             //
##   ("hello") -> "he"                                                       //
##   ("hi") -> "hi"                                                          //
##   ("h") -> "h@"                                                           //
##/////////////////////////////////////////////////////////////////////////////

# Input the values
str = input()

# Print the output
if len(str) >= 2:
    print(str[:2])
elif len(str) == 1:
    print(str[:1], "@", sep="")
else:
    print("@@")