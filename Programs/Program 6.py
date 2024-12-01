x = int(input("Enter a number: "))
if x<0:
    print("Factorial is not defined for negative numbers.")
elif x==0:
    print("The factorial of", x, "is 1")
else:
    y = 1
    for i in range(1, x+1):
        y = y*i
    print("The factorial of", x, "is", y)
