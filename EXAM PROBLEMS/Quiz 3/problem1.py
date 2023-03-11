# Prompt user to input a the file names.
file_read = input("Source file name: ")
file_write = input("Target file name: ")

# Open the file to read and write:
while True:
    try:
        f_read = open(file_read, mode = 'r')
        f_write = open(file_write, mode = 'w')
        break
    except:
        print("Error: File cannot be opened")
        file_read = input("Source file name: ")
        file_write = input("Target file name: ")


# Loop over the file and write all strings not starting with number.
for line in f_read:
    if not line[0].isdigit():
        f_write.write(line)

# Clsoe the files.
f_read.close()
f_write.close()