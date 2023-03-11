from PyTest import *
##///////////// PROBLEM STATEMENT /////////////
## Write Python code which, when it reads    // 
## two input boolean values, produces the    //
## following results:                        //
##                                           //
##   True True   -> False                    //
##   True False  -> False                    //
##   False True  -> True                     //
##   False False -> False                    //
##/////////////////////////////////////////////

# Input the values
a = input()
b = input()

# Convert to real boolean values
if a == "True":
    a = True
else:
    a = False

if b == "True":
    b = True
else:
    b = False

# Create the if statements to print the results.
if a == False and b == True:
    print("True")
else:
    print("False")