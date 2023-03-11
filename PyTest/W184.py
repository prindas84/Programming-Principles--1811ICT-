from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given a string, print the string made of its first two chars, so the      //
## String "Hello" yields "He". If the string is shorter than length 2, print //
## whatever there is, so "X" yields "X", and the empty string "" yields the  //
## empty string "".                                                          //
##   "Hello" -> "He"                                                         //
##   "abcdefg" -> "ab"                                                       //
##   "ab" -> "ab"                                                            //
##/////////////////////////////////////////////////////////////////////////////

str = input()

if len(str) < 2:
    print(str)
else:
    print(str[0], str[1], sep="")