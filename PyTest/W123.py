from PyTest import *
##//////////////////// PROBLEM STATEMENT ////////////////////////
## Given a 24 hour time of day as hours minutes seconds, add   //
## a time interval which is specified as hours minutes seconds //
##                                                             //
##   hrs mins secs hrs mins secs    hrs mins secs              // 
##   13   24   30   2   40   40  -> 16    5   10               //
##///////////////////////////////////////////////////////////////

hrs = int(input())
mins = int(input())
secs = int(input())
int_hrs = int(input())
int_mins = int(input())
int_secs = int(input())

new_hrs, new_mins, new_secs = 0, 0, 0

# Calculate the new seconds.
if secs + int_secs >= 60:
    new_secs = secs + int_secs - 60
    mins += 1
else:
    new_secs = secs + int_secs

# Calculate the new minutes.
if mins + int_mins >= 60:
    new_mins = mins + int_mins - 60
    hrs += 1
else:
    new_mins = mins + int_mins

# Calculate the new hours.
if hrs + int_hrs >= 24:
    new_hrs = hrs + int_hrs - 12

else:
    new_hrs = hrs + int_hrs

print(new_hrs, new_mins, new_secs)