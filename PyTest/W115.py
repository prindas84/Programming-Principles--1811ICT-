from PyTest import *
##////////////////////// PROBLEM STATEMENT ////////////////////////////
## Print out the cost of a phone call, given the connection cost,    //
## the cost per minute and the length of the call, in minutes. The   //
## cost is the connection cost plus the cost per minute times the    //
## length of the call.                                               //
##                                                                   //
##   Connection Cost   Cost/Minute   Call Length      Call Cost      //
##         10              2             20       ->     50          //       
##/////////////////////////////////////////////////////////////////////

connectionCost = int(input())
cost_minute = int(input())
length = int(input())

print(cost_minute * length + connectionCost)