from PyTest import *
##////////////////////// PROBLEM STATEMENT //////////////////////
## You are driving a little too fast, and a police officer     //
## stops you. Write code to compute the result, encoded as an  //
## int value: 0=no ticket, 1=small ticket, 2=big ticket. If    //
## speed is 60 or less, the result is 0. If speed is between   //
## 61 and 80 inclusive, the result is 1. If speed is 81 or     //
## more, the result is 2. Unless it is your birthday -- on     //
## that day, your speed can be 5 higher in all cases.          //
##                                                             //
##  Speed  Birthday  Result                                    //
##   60    False   ->   0                                      //
##   65    False   ->   1                                      //
##   65    True   ->    0                                      //
##///////////////////////////////////////////////////////////////

# Input the values.
speed = int(input())
birthday = input()

# BIRTHDAY FALSE
# If the speed is 60 or less - Result = 0.
# If the speed 61 - 80 Inclusive - Result = 1.
# If the speed greater than 81 - Redult = 2
if birthday == "False":
    if speed <= 60:
        print(0)
    elif 61<speed<=80:
        print(1)
    else:
        print(2)

# Else, if it is your birthday, you can go 5 more.
else:
    if speed <= 65:
        print(0)
    elif 66<speed<=85:
        print(1)
    else:
        print(2)
