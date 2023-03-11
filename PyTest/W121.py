from PyTest import *
##/////////////////////////// PROBLEM STATEMENT /////////////////////////////
## Write a program which accepts a time interval in seconds and prints the //
## equivalent time in hours minutes seconds. One hour is 3600 seconds and  //
## one minute is 60 seconds.                                               //
##                                                                         //
##   Total seconds     hours  minutes  seconds                             //
##       3680       ->   1      10        20                               //       
##///////////////////////////////////////////////////////////////////////////

total = int(input())

hours = total // 3600
minutes = total // 60
seconds = total - hours * 3600 - minutes * 60

print(hours, minutes, seconds)