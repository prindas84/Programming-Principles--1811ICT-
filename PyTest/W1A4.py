from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given two strings, append them together (known as "concatenation") and    //
## print the result. However, if the  concatenation creates a double-char,   //
## then omit one of the chars, so "abc" and "cat" yields "abcat".            //
##   "abc", "cat" -> "abcat"                                                 //
##   "dog", "cat" -> "dogcat"                                                //
##   "abc", "" -> "abc"                                                      //
##/////////////////////////////////////////////////////////////////////////////

str_one = input()
str_two = input()

if str_one[-1] == str_two[0]:
    print(str_one[:-1], str_two, sep="")
else:
    print(str_one, str_two, sep="")