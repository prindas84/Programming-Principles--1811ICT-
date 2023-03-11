from PyTest import *
##////////////////////// PROBLEM STATEMENT ////////////////////////////
## Write Python code which, given an integer grade, prints "Pass" if //
## the grade is greater than or equal to 50 but less than or equal   //
## to 100. If the grade is greater than or equal to 0 and less than  //
## 50 it prints "Failed" otherwise it prints "Illegal Grade".        //
##   -10 -> Illegal Grade                                            //
##   23 -> Failed                                                    //
##   50 -> Passed                                                    //
##   78 -> Passed                                                    //
##   128 -> Illegal Grade                                            //
##/////////////////////////////////////////////////////////////////////

# Input the value

grade = int(input())

# If grade greater than 50 AND less than and equal to 100 - Print "Pass"
# Else if grade greater than or equal to 0 AND less than 50 - Print "Fail"
# Else - Print "Illegal Grade"

if grade >= 50 and grade <= 100:
    print("Passed")
elif grade >= 0 and grade < 50:
    print("Failed")
else:
    print("Illegal Grade")