from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given two strings, print True if either of the strings appears at the     //
## very end of the other string, ignoring upper/lower case differences       //
## (in other words, the computation should not be "case sensitive").         //
##   "Hiabc", "abc" -> True                                                  //
##   "AbC", "HiaBc" -> True                                                  //
##   "abc", "abXabc" -> True                                                 //
##   "abc", "abXaXc" -> False                                                //
##/////////////////////////////////////////////////////////////////////////////

str_one = input()
str_two = input()

if str_one <= str_two:
    long = str_one.lower()
    short = str_two.lower()
else:
    long = str_two.lower()
    short = str_one.lower()

length = len(short)

if long[-length:] == short:
    print("True")
else:
    print("False")