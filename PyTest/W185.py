from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given 2 strings, a and b, print a string of the form short+long+short,    //
## with the shorter string on the outside and the longer string on the       //
## inside. The strings will not be the same length, but they may be empty    //
## (length 0).                                                               //
##   "Hello", "hi" -> "hiHellohi"                                            //
##   "hi", "Hello" -> "hiHellohi"                                            //
##   "aaa", "b" -> "baaab"                                                   //
##/////////////////////////////////////////////////////////////////////////////

str_one = input()
str_two = input()

if len(str_one) < len(str_two):
    print(str_one, str_two, str_one, sep="")
else: print(str_two, str_one, str_two, sep="")