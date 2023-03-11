# Matthew Prendergast
# 3rd May, 2022 - Problem 4 (Workshop - Week 6)

# Prompt user to input a a list of students and scores.
input_one = input("Student 1 (courses 1-4): ")
input_two = input("Student 2 (courses 1-4): ")
input_three = input("Student 3 (courses 1-4): ")
input_four = input("Student 4 (courses 1-4): ")
input_five = input("Student 5 (courses 1-4): ")

# Append the scores into a 2D list of students.
students = []
students.append(input_one.split(" "))
students.append(input_two.split(" "))
students.append(input_three.split(" "))
students.append(input_four.split(" "))
students.append(input_five.split(" "))

# Convert the list to integers.
for i in range(len(students)):
    for j in range(len(students[i])):
        students[i][j] = int(students[i][j])

# Initialise the variables for the highest scores.
high_student, high_course= 0, 0

# Find the highest student score.
for i in range(5):
    if sum(students[i]) / len(students[i]) > high_student:
        high_student = sum(students[i]) / len(students[i])

# Find the highest course score.
for i in range(4):
    count = 0
    for j in range(5):
        count = count + students[j][i]
    if count / 5 > high_course:
        high_course = count / 5

print("The highest average mark of students:", high_student)
print("The highest average mark of courses:", high_course)