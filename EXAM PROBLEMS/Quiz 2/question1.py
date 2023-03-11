id = input("Enter an ID: ")

count = 1

while len(id) >= 4:
    count += 1
    id = input("Enter an ID: ")

print(f"{count} IDs were entered.")