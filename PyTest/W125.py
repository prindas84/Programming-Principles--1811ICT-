from PyTest import *
##//////////////////////////// PROBLEM STATEMENT /////////////////////////////
## Write a Python program that, given a cost of an item (less than or equal //
## to one dollar), gives the number of 50 cent, 20 cent, 10 cent, 5 cent    //
## and 1 cent coins the buyer would receive if they handed over one dollar. //
## You must minimise the number of coins in the change.                     //
##////////////////////////////////////////////////////////////////////////////

price = int(input())
value = 100 - price
fifty, twenty, ten, five, one = 0, 0, 0, 0, 0

if value >= 50 and value > 0:
    fifty = value // 50
    value -= 50

if value >= 20 and value > 0:
    twenty = value // 20
    value -= 20 * twenty

if value >= 10 and value > 0:
    ten = value // 10
    value -= 10 * ten

if value >= 5 and value > 0:
    five = value // 5
    value -= 5 * five

if value >= 1 and value > 0:
    one = value // 1

print(fifty, twenty, ten, five, one)