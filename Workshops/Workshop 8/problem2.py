# Matthew Prendergast
# 17th May, 2022 - Problem 2 (Workshop - Week 8)

# Define the sorting function.
def sort_list(x, y):
    sorted = []
    i, j = 0, 0
    while i < len(x) and j < len(y):
        if x[i] == y[j]:
            if x[i] not in sorted:
                sorted.append(x[i])
            i += 1
            j += 1
        elif x[i] < y[j]:
            i += 1
        else:
            j += 1
    
    print(sorted)

# Prompt user to input a a list of numbers.
l_one = input("List 1: ")

while l_one:
    l_two = input("List 2: ")

    # Convert the inputs to lists.
    l_one = l_one.split(" ")
    l_two = l_two.split(" ")

    # Convert to the lists to integer lists.
    for i in range(len(l_one)):
        l_one[i] = int(l_one[i])
    for i in range(len(l_two)):
        l_two[i] = int(l_two[i])

    # Sort the lists.
    l_one.sort()
    l_two.sort()

    sort_list(l_one, l_two)

    l_one = input("List 1: ")