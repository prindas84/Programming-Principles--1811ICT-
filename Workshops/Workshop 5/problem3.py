# Matthew Prendergast
# 22nd April, 2022 - Problem 3 (Workshop - Week 5)

def checkLeap(year):
    """This function returns True if the year is a leap year."""
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def countDays(start, finish):
    """This function counts how many days between the first ans second year
    
       The function will check each individual year to see if it is a leap year
       then increment the count accordingly"""

    count = 0
    for i in range(start, finish + 1):
        if checkLeap(i):
            count += 366
        else:
            count += 365
    return count

# Retrieve the user input.
year_one = int(input("Year 1? "))
year_two = int(input("Year 2? "))

# Print the result.
print("Number of days:", countDays(year_one, year_two))
