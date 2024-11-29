x = int(input("Enter a number: "))
y = 1

if x < 0:
    print("Factorial is not defined for negative numbers.")
elif x == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, x + 1):
        y*= i
    print(f"The factorial of {x} is {y}.")
