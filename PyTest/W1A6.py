from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given a string, print a version without the first 2 chars. Except keep    //
## the first char if it is 'a' and keep  the second char if it is 'b'. The   //
## string may be any length.                                                 //
##   "Hello" -> "llo"                                                        //
##   "java" -> "va"                                                          //
##   "away" -> "aay"                                                         //
##/////////////////////////////////////////////////////////////////////////////

str = input()

if str[0] == "a":
    print("a", end="")
if str[1] == "b":
    print("b", end="")

print(str[2:])