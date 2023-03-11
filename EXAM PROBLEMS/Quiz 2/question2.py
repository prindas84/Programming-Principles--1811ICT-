def pattern(number):
    count = 1

    while number > 0:
        print("+" * number, "o" * count, sep="")
        count += 1
        number -= 1

n = int(input("Number of rows: "))

pattern(n)