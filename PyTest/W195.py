from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given three inputs - two strings (word and separator) and one integer     //
## (count), print a string made of count occurences of the word, separated   //
## by the separator string.                                                  //
##   "Word", "X", 3   -> "WordXWordXWord"                                    //
##   "This", "And", 2 -> "ThisAndThis"                                       //
##   "This", "And", 1 -> "This"                                              //
##/////////////////////////////////////////////////////////////////////////////

str_one = input()
str_two = input()
count = int(input())

for i in range(count):
    print(str_one, end="")
    if i != count - 1:
       print(str_two, end="")
    else:
        break
 