from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Print True if the string "cat" and "dog" appear the same number of times  //
## in the given string.                                                      //
##   "catdog" -> True                                                        //
##   "catcat" -> False                                                       //
##   "1cat1cadodog" -> True                                                  //
##/////////////////////////////////////////////////////////////////////////////

# Input the variables from the test file.
str = input()

# Set the variables to zero
catCount = str.count("cat")
dogCount = str.count("dog")

# Print the results.
if catCount == dogCount:
    print("True")
else:
    print("False")