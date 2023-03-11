from PyTest import *
##///////////////////// PROBLEM STATEMENT /////////////////////
## Given an int list, print True if it contains a 2 or a 3.  //
##    2, 5  -> True                                          //
##    4, 3  -> True                                          //
##    4, 5  -> False                                         //
##/////////////////////////////////////////////////////////////

l = int(input())
ls = []

for i in range(l):
    t = int(input())
    ls.append(t)

if 2 in ls or 3 in ls:
    print("True")
else:
    print("False")