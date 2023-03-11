# Matthew Prendergast
# 24th May, 2022 - Problem 1 (Workshop - Week 9)

def input_var(var, val):
    """This function inputs a key and a value to the dictionary"""
    global input_variable
    input_variable[var] = int(val)

    return

def input_print(var):
    """This function prints something to the screen given a certain input"""
    global input_variable
    if var.isdigit():
        print(var)
    elif var in input_variable:
        print(f"{var} equals {input_variable[var]}")
    else:
        print(f"{var} is undefined.")

    return

def input_gets(var, val):
    """This function assigns variables new values using the get keyword"""
    global input_variable
    if var.isalpha():
        if val.isdigit():
            input_var(var, val)
        elif val in input_variable:
            val_temp = input_variable[val]
            input_var(var, val_temp)
        else:
            print("Syntax error.")
    else:
        print("Syntax error.")

    return

def input_adds(var, val):
    """This function adds values to variables using the adds keyword"""
    global input_variable
    if var.isalpha():
        if val.isdigit():
            input_variable[var] = input_variable[var] + int(val)
        elif val in input_variable:
            val_temp = input_variable[val]
            input_variable[var] = input_variable[var] + val_temp
        else:
            print("Syntax error.")
    else:
        print("Syntax error.")
        
    return

def main():
    """This is the main program code"""

# Initialise the empty dictionary.
input_variable = {}

# Get the initial input from the user.
print("Welcome to the Adder REPL.")
statement = input("??? ")
statement = statement.strip().lower()

# If the user does not want to quit the program, proceed.
while statement != "quit":

    # Split the statement into a list to be read.
    state_list = statement.split()

    # If the user wants to input a variable.
    if len(state_list) == 2 and state_list[0] == "input":
        var = state_list[1]
        if var.isalpha():
            val = input(f"Enter a value for {var}: ")
            while not val.isdigit():
                val = input(f"Enter a value for {var}: ")

            input_var(var, val)

    # If the user wanted to print something to the screen.
    elif len(state_list) == 2 and state_list[0] == "print":
        var = state_list[1]
        input_print(var)

    # If the user wants to assign a variable with gets keyword.
    elif len(state_list) == 3 and state_list[1] == "gets":
        var = state_list[0]
        val = state_list[2]
        input_gets(var, val)

    # If the user wants to add two variables with adds keyword.
    elif len(state_list) == 3 and state_list[1] == "adds":
        var = state_list[0]
        val = state_list[2]
        input_adds(var, val)

    else:
        print("Syntax error.")

    # Repromt the user for a new input.
    statement = input("??? ")
    statement = statement.strip().lower()

# Print Goodbye on the exit.
print("Goodbye.")

# This calls the main function.
main()
