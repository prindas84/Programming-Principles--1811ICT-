from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Start with 2 int lists, a and b. Consider the sum of the values in each   //
## list.  Print the list which has the largest sum. In event of a tie,       //
## print a.                                                                  //
##    1, 2    3, 4  ->  3, 4                                                 //
##    3, 4    1, 2  ->  3, 4                                                 //
##    1, 1    1, 2  ->  1, 2                                                 //
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

if sum(ls) >= sum(ls_two):
    print(ls)
else:
    print(ls_two)