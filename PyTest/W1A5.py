from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given two strings, append them together (known as "concatenation") and    //
## print the result. However, if the strings are different lengths, omit     //
## chars from the longer string so it is the same length as the shorter      //
## string. So "Hello" and "Hi" yield "loHi". The strings may be any length.  //
##                                                                           //
##   "Hello", "Hi" -> "loHi"                                                 //
##   "Hello", "java" -> "ellojava"                                           //
##   "java", "Hello" -> "javaello"                                           //
##/////////////////////////////////////////////////////////////////////////////

str_one = input()
str_two = input()

if len(str_one) >= len(str_two):
    length = len(str_two)
    print(str_one[-length:], str_two, sep="")
else:
    length = len(str_one)
    print(str_one, str_two[-length:], sep="")

 