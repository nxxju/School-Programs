x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
z = float(input("Enter the third number: "))

if x >= y and x >= z:
    largest = x
elif y >= x and y >= z:
    largest = y
else:
    largest = z

print("The largest number is:", largest)
