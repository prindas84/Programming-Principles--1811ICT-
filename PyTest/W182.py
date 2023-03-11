from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given a string, print a new string made of 3 copies of the first 2 chars  //
## of the original string. The string may  be any length. If there are fewer //
## than 2 chars, use whatever is there.                                      //
##   "Hello" -> "HeHeHe"                                                     //
##   "ab" -> "ababab"                                                        //
##   "H" -> "HHH"                                                            //
##/////////////////////////////////////////////////////////////////////////////

str = input()

if len(str) == 1:
    print(str * 3)
else:
    print(str[:2] * 3)