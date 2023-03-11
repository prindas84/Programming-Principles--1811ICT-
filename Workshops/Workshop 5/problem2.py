# Matthew Prendergast
# 22nd April, 2022 - Problem 2 (Workshop - Week 5)

def stringConvert(s):
    """The function converts digits in a string to _
    
       s is the string which is passed into the function
       new_string is the new string which is constructed and returned"""

    new_string = ""
    for char in s:
        if char.isdigit():
            new_string = new_string + "_"
        else:
            new_string = new_string + char
    return new_string

# Retrieve the user input.
sentance = input("Input a string? ")

# Print the output.
print("Output:", stringConvert(sentance))