from PyTest import *
##/////////////////// PROBLEM STATEMENT /////////////////////////
## Given a 12 hour time of day as hours minutes seconds pm,    //
## add a time interval which is specified as hours minutes     //
## seconds. The input pm is 0 for morning and 1 afternoon.     //
##                                                             //
##   hrs mins secs am/pm  hrs mins secs    hrs mins secs am/pm //
##    1   24   30    1     2   40   40  ->  4   5    10    1   //
##///////////////////////////////////////////////////////////////

# Original Time
hrs = int(input())
mins = int(input())
secs = int(input())
am_pm = int(input())

# Increment Values
inc_hrs = int(input())
inc_mins = int(input())
inc_secs = int(input())

# New Time
new_hrs = 0
new_mins = 0
new_secs = 0

# Calculate New Time
if secs + inc_secs > 60:
    mins += 1
    new_secs = secs + inc_secs - 60
else:
    new_secs = secs + inc_secs

if mins + inc_mins > 60:
    hrs += 1
    new_mins = mins + inc_mins - 60
else:
    new_mins = mins + inc_mins

if hrs + inc_hrs > 12 and am_pm == 1:
    am_pm = 0
    new_hrs = hrs + inc_hrs - 12
elif hrs + inc_hrs > 12 and am_pm == 0:
    am_pm = 1
    new_hrs = hrs + inc_hrs - 12
else:
    new_hrs = hrs + inc_hrs

print(new_hrs, new_mins, new_secs, am_pm)

