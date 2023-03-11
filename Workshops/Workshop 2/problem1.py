# Matthew Prendergast
# 30th March, 2022 - Problem 1 (Workshop - Week 2)

# Store the user inputs into variables. Cast to a float.
length = float(input("Length of park (m): "))
width = float(input("Width of park (m): "))
litres = float(input("Litres per square metre: "))

# Print the results.
print("Litres required = ", length * width * litres)