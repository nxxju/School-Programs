# Program to display the multiplication table of a number entered by the user.

x = int(input("Enter a number: "))

print("Multiplication table of", x, ":")
for i in range(1, 11):
    print(x, "x", i, "=", x * i)
