x = []

n = int(input("Numbers to enter:- "))

for _ in range(n):
    number = int(input("Enter an integer: "))
    
    if number % 2 == 0:
        x.append(number)

print("List of even numbers:", x)
