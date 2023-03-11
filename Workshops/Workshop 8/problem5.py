# Matthew Prendergast
# 18th May, 2022 - Problem 5 (Workshop - Week 8)

# Define a function to print each result.
def print_line(ls, infected):
    print(f"{ls[0]:<5}", end=" ")
    for name in infected:
        print(name, end=" ")
    print(len(infected))

# Prompt the user to input the file name.
file_name = input("Enter file name: ")

# Try to open the file.
while True:
    try:
        f_read = open(file_name, mode="r")
        break
    except:
        print("Error: Could not open the file.")
        file_name = input("Enter file name: ")

begin = False
infected = []

# Read each line of the file.
for line in f_read:
    ls = []
    temp_infected = []

    # If the * for the first infected person has been found, begin the process of finding the rest.
    if begin:

        # Read in a line without the \n character and create a new list.
        ls = line[:-1].split(" ")

        # Create a new list of names without the week number.
        names = ls[1:]

        # Create a temporary infected list, so it keeps the original checking list the same when new names are added.
        temp_infected += infected
        for name in temp_infected:

            # If the name of an infected person is at the table, add those to the left and right to the 
            # original infected list.
            if name in names:
                count = names.index(name)

                # If the person is at the end of the list, the person to their right will be at the start of the list.
                # Else, add the person to the left and right.
                if count == len(names) - 1:
                    if names[0] not in temp_infected:
                        infected.append(names[0])
                elif names[count + 1] not in temp_infected:
                    infected.append(names[count + 1])
                if names[count - 1] not in temp_infected:
                    infected.append(names[count - 1])
            
        print_line(ls, infected)

    # If the first infected person hasn't been found yet.
    if not begin:
    
        # To find the first infected person we will look for the asterisk in the line.
        if "*" in line:

            # Once found, flag the being as True to begin checking all rounds after this itteration.
            begin = True

            # Read in a line without the \n character and create a new list.
            ls = line[:-1].split(" ")

            # Create a new list of names without the week number.
            names = ls[1:]
            count = 0

            # Check to find the exact name that is infected, who has an asterisk against their name.
            for name in names:
                if "*" in name:

                    # Once found, add the person to the infected list, and the people to their left and right.
                    infected.append(name[:-1])
                    infected.append(names[count - 1])

                    # If the person is at the end of the list, the person to their right will be at the start of the list.
                    if count == len(names) - 1:
                        infected.append(names[0])
                        break
                    else:
                        infected.append(names[count + 1])
                        break
                count += 1
                
            print_line(ls, infected)
    



