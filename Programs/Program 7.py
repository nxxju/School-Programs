x = int(input("Enter a number: "))

print("Multiplication table of", x, ":")
for i in range(1, 11):
    print(x, "x", i, "=", x * i)
