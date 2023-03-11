from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## We'll say that a lowercase 'g' in a string is "happy" if there is another //
## 'g' immediately to its left or right.  Print True if all the g's in the   //
## given string are happy.                                                   //
##   "xxggxx" -> True                                                        //
##   "xxgxx" -> False                                                        //
##   "xxggyygxx" -> False                                                    //
##/////////////////////////////////////////////////////////////////////////////

# Prompt user to input a string of letters.
str = input("String: ")
happy = "False"

# If the length of the string is more than 1 character, and G is in the string.
if "g" in str and len(str) > 1:

    # Compare every charter, except the last, to the next charter, and the previous character in the string.
    for i in range(len(str) - 1):
        if str[i] == "g":
            if str[i + 1] == "g" or str[i - 1] == "g":
                happy = "True"
            else:
                happy = "False"
                break
    
    # Check the last character before finishing.
    if str[-1] == "g" and str[-2] != "g":
        happy = "False"

# Print the result.
print(happy)