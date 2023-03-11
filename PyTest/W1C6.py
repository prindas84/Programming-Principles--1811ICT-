from PyTest import *
##//////////////////////////// PROBLEM STATEMENT ///////////////////////////////
## Print a list that contains the exact same numbers as the given list,       //
## but rearranged so that all the even numbers come before all the odd        //
## numbers. Other than that, the numbers can be in any order. You must modify //
## and print the given list (no additional data structures).                  //
##   1, 0, 1, 0, 0, 1, 1 -> 0, 0, 0, 1, 1, 1, 1                               //
##   3, 3, 2 -> 2, 3, 3                                                       //
##   2, 2, 2 -> 2, 2, 2                                                       //
##//////////////////////////////////////////////////////////////////////////////

l = int(input())
ls = []

for i in range(l):
    t = int(input())
    ls.append(t)

list_two = []

for i in range(len(ls)):
    if ls[i] % 2 == 0:
        list_two.append(ls[i])

for j in range(len(ls)):
    if ls[j] % 2 != 0:
        list_two.append(ls[j])

print(list_two)