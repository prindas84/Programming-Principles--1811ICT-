from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given a list of ints, print True if 6 appears as either the first or      //
## last element in the list. The list will be length 1 or more.              //
##    1, 2, 6  -> True                                                       //
##    6, 1, 2, 3  -> True                                                    //
##    3, 2, 1 -> False                                                       //
##/////////////////////////////////////////////////////////////////////////////

l = int(input())
ls = []

for i in range(l):
    t = int(input())
    ls.append(t)

if ls[0] == 6 or ls[-1] == 6:
    print("True")
else:
    print("False")

