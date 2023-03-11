# Matthew Prendergast
# 7th May, 2022 - Problem 1 (Workshop - Week 7)

# Prompt user to input a the file names.
file_read = input("Source file name: ")
file_write = input("Target file name: ")

# Initialise the count to 0.
count = 0

# Open a file to read and create a file to write to.
f_read = open(file_read, mode = 'r')
f_write = open(file_write, mode = 'w')

# Loop over the file and write all non-empty strings. Incerment count for all empty strings.
for line in f_read:
    if line != "\n":
        f_write.write(line)
    else:
        count += 1

# Print the result.
print("Lines removed:", count)

f_read.close()
f_write.close()