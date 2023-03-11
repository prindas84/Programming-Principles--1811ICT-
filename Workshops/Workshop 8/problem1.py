# Matthew Prendergast
# 17th May, 2022 - Problem 1 (Workshop - Week 8)

# Define the rotation function.
def rotate(numbers):
    """ The function will take in a list of numbers and rearrange it until it is back to its original"""
    temp = []
    for i in range(len(numbers)):
        for j in range(1, len(numbers)):
            temp.append(numbers[j])
        temp.append(numbers[0])
        print(temp)
        numbers = temp
        temp = []

# Prompt user to input a a list of numbers.
ls = input("Input a list: ")

# Convert the input to a list.
num_list = ls.split(" ")

for i in range(len(num_list)):
    num_list[i] = int(num_list[i])

print(num_list)
rotate(num_list)

