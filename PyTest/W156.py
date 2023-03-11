from PyTest import *
##///////////////////// PROBLEM STATEMENT /////////////////////////
## Normally you answer, except in the morning you only answer if //
## it is your mum calling. In all cases, if you are asleep, you  //
## do not answer.                                                //
##                                                               //
##  Morning  Mum   Asleep    Result                              //
##   False  False  False  -> True                                //
##   False  False  True   -> False                               //
##   True   False  False  -> False                               //
##/////////////////////////////////////////////////////////////////

# Input the values
morning = input()
mum = input()
asleep = input()

# If Asleep = TRUE, Morning = TRUE and Mum = FALSE - Print False. Else True.
if asleep == "True" or (morning == "True" and mum == "False"):
    print("False")
else:
    print("True")
