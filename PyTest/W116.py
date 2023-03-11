from PyTest import *
##/////////////////////////// PROBLEM STATEMENT /////////////////////////
## Write a program which accepts a time interval in hours, minutes and //
## seconds and prints the equivalent time in just seconds. One hour is //
## 3600 seconds and one minute is 60 seconds.                          //
##                                                                     //
##   hours  minutes  seconds     Total seconds                         //
##     1       10       20    ->    4220                              //
##///////////////////////////////////////////////////////////////////////

hours = int(input())
minutes = int(input())
seconds = int(input())

print(hours * 3600 + minutes * 60 + seconds)