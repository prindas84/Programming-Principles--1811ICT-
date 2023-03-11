from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given a string, print True if "bad" appears starting at index 0 or 1 in   //
## the string, such as with "badxxx" or  "xbadxx" but not "xxbadxx". The     //
## string may be any length, including 0.                                    //
##   "badxx" -> True                                                         //
##   "xbadxx" -> True                                                        //
##   "xxbadxx" -> False                                                      //
##/////////////////////////////////////////////////////////////////////////////

str = input()

if len(str) >= 3:
    if str[0:3] == "bad" or str[1:4] == "bad" and "bad" not in str[2:]:
        print("True")
    else:
        print("False")
else:
    print("False")
