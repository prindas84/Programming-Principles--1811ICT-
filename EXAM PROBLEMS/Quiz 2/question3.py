number_list = [2,4,6,5,8,10,2,4,12]

total = 0
count = 0

if len(number_list) > 3:
    for i in range(len(number_list)):
        if number_list[i] % 2 == 0:
            count += 1
        else:
            if count >= 3:
                total += 1
            count = 0
if count >= 3:
    total += 1

print("Output:", total)

    


