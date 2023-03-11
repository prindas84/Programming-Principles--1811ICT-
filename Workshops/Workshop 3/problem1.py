# Matthew Prendergast
# 1st April, 2022 - Problem 1 (Workshop - Week 3)

# Input the grade.
grade = float(input("How many marks? "))

# Less than 50 marks = F
if grade < 50:
    print("Grade awarded: F")

# Equal to 50 but less than 65 marks = 485
elif grade < 65:
    print("Grade awarded: 4")

# Equal to 65 but less than 75 marks = 5
elif grade < 75:
    print("Grade awarded: 5")

# Equal to 75 but less than 85 marks = 6
elif grade < 85:
    print("Grade awarded: 6")

# All marks above 85 marks = 7
else:
    print("Grade awarded: 7")