from PyTest import *
##////////////////////////////// PROBLEM STATEMENT /////////////////////////////
## Write Python code that reads two integers from the keyboard. Given two     //
## inclusive ranges -8..-4 and 10..16 print True if both integers are in one  //
## of these ranges or both integers are not in these ranges. Otherwise print  //
## False.                                                                     //
## You must not use the Python if or if-else statement.                       //
##                                                                            //
## All ranges are inclusive                                                   //
##                                                                            //
## Example inputs/outputs are:                                                //
##    10 50   -> False                                                        //
##    20 5    -> True                                                         //
##    100 20  -> True                                                         //
##    -5 20   -> False                                                        //
##    -5 12   -> True                                                         //
##    -10 0   -> True                                                         //
##//////////////////////////////////////////////////////////////////////////////

# Input the values

a = int(input())
b = int(input())

# IF both integers are in one of the ranges -8..-4 and 10..16 - PRINT TRUE
# IF both integers are NOT IN the ranges - PRINT TRUE
# ELSE - PRINT FALSE

print(((-8<=a<=-4 or 10<=a<=16) and (-8<=b<=-4 or 10<=b<=16)) or ((a<-8 or -4<a<10 or a>16) and (b<-8 or -4<b<10 or b>16)))