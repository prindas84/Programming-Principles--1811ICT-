from PyTest import *
##///////////// PROBLEM STATEMENT /////////////
## Write Python code which, when it reads    // 
## two input boolean values, produces the    //
## following results:                        //
##                                           //
##   True True   -> True                     //
##   True False  -> False                    //
##   False True  -> False                    //
##   False False -> True                     //
##/////////////////////////////////////////////

# Input the values
a = input()
b = input()

# Convert the strings to real boolean values
if a == "True":
    a = True
else:
    a = False

if b == "True":
    b = True
else:
    b = False

# Create the statments to print the correct results
if a == b:
    print(True)
else:
    print(False)