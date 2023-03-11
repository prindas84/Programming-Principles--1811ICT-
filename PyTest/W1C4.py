from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given 2 lists of ints, a and b, print True if they have the same first    //
## element or they have the same last element. Both lists will be length 1   //
## or more.                                                                  //
##    1, 2, 3    7, 3  -> True                                               //
##    1, 2, 3    7, 3, 2  -> False                                           //
##    1, 2, 3    1, 3  -> True                                               //
##/////////////////////////////////////////////////////////////////////////////

l = int(input())
ls = []

for i in range(l):
    t = int(input())
    ls.append(t)

l_two = int(input())
ls_two = []

for j in range(l_two):
    y = int(input())
    ls_two.append(y)

if ls[0] == ls_two[0] or ls[-1] == ls_two[-1]:
    print("True")
else:
    print("False")