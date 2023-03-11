file_read = input("File name: ")

while True:
    try:
        f_read = open(file_read, mode = "r")
        break
    except:
        print("Error: File cannot be opened")
        file_read = input("File name: ")

count = 0

for line in f_read:
    words = line.split()
    for word in words:
        if len(word) >= 4:
            # if "file" in word: would have been better
            if word[0].lower() == "f" and word[1].lower() == "i" and word[2].lower() == "l" and word[3].lower() == "e":
                count += 1

print("The string 'file' appears", count, "times")

# f_read.close() - Forgot this.
