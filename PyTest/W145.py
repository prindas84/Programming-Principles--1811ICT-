from PyTest import *
##//////////////////// PROBLEM STATEMENT //////////////////////////
## Given a number n, print True if n is in the range 1..10,      //
## inclusive. Unless "outsideMode" is True, in which case print  //
## True if the number is less or equal to 1, or greater or equal //
## to 10.                                                        //
##   5, False -> True                                            //
##   11, False -> False                                          //
##   11, True -> True                                            //
##/////////////////////////////////////////////////////////////////

# Input the values
intValue = int(input())
boolValue = input()

# Satisfy the condition if the bool value is True.
if boolValue == "True":
    boolValue = True
else:
    boolValue = False

# Satifsfy the rest of the conditions.
if boolValue == False and 1<=intValue<=10:
    print("True")
elif boolValue == True and (intValue <= 1 or intValue >= 10):
    print("True")
else:
    print("False")