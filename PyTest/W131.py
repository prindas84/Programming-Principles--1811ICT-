from PyTest import *
##///////////// PROBLEM STATEMENT /////////////
## Write Python code which, when it reads    // 
## two input boolean values, produces the    //
## following results:                        //
##                                           //
##   True True   -> False                    //
##   True False  -> False                    //
##   False True  -> False                    //
##   False False -> True                     //
##/////////////////////////////////////////////

a = input()
b = input()

if a == "True":
    a = bool(1)
else:
    a = bool(0)

if b == "True":
    b = bool(1)
else:
    b = bool(0)

if a and b or a and not b or not a and b:
    print(False)
else:
    print(True)



