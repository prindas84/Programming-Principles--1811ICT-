from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given a string, print True if the first 2 chars in the string also appear //
## at the end of the string, such as with "edited".                          //
##   "edited" -> True                                                        //
##   "edit" -> False                                                         //
##   "ed" -> True                                                            //
##/////////////////////////////////////////////////////////////////////////////

str = input()

if len(str) >= 2:
    if str[:2] == str[-2:]:
        print("True")
    else:
        print("False")
else:
    print("False")