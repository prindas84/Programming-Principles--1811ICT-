from PyTest import *
##////////////////////////////// PROBLEM STATEMENT /////////////////////////////
## Write Python code that reads a boolean and an integer from the keyboard.   //
## If the boolean is True and the integer is in the range 1. . 100 OR if      //
## the boolean is False and the integer is not in the range 1..100 and the    //
## integer is not in the range -20..-8 print True. Otherwise print False.     //
## You must not use the Python if or if-else statement.                       //
##                                                                            //
## All ranges are inclusive                                                   //
##                                                                            //
## Example inputs/outputs are:                                                //
##    True 50   -> True                                                       //
##    True -5   -> False                                                      //
##    False 50  -> False                                                      //
##    False 200 -> True                                                       //
##    False -5  -> True                                                       //
##//////////////////////////////////////////////////////////////////////////////

# Input a boolean and an integer
boolValue = input()
intValue = int(input())

# Convert the strings to real boolean values
if boolValue == "True":
    boolValue = True
else:
    boolValue = False

# IF the boolean is *true* AND the integer IS 1-100. - PRINT TRUE
# OR if the boolean is *false* AND the integer IS NOT 1-100....AND the integer IS NOT -20 - -8. - PRINT TRUE
# ELSE PRINT FALSE
print(boolValue and 1<=intValue<=100 or not boolValue and (intValue < 1 or intValue > 100) and (intValue < -20 or intValue > -7))


