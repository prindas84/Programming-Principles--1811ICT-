# Matthew Prendergast
# 18th May, 2022 - Problem 4 (Workshop - Week 8)

def sort_list(x, y):

    # Sort the lists.
    x.sort(reverse=True)
    y.sort(reverse=True)

    # Merge the lists into one.
    i, j = 0, 0
    new_list = []

    while i < len(x) and j < len(y):
        if x[i] == y[j]:
            new_list.append(x[i])
            new_list.append(y[j])
            i += 1
            j += 1
        elif x[i] > y[j]:
            new_list.append(x[i])
            i += 1
        else:
            new_list.append(y[j])
            j += 1
        
        if i < len(x) and j >= len(y):
            for g in range(i, len(x)):
                new_list.append(x[g])
        elif j < len(y) and i >= len(x):
            for h in range(j, len(y)):
                new_list.append(y[h])
    
    return new_list

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

    print(sort_list(l_one, l_two))

    l_one = input("List 1: ")