# Program to ask the user to provide the integer inputs to make a list. Store only the even values given and print the list.

x = []

n = int(input("Numbers to enter:- "))

for _ in range(n):
    number = int(input("Enter an integer: "))
    
    if number % 2 == 0:
        x.append(number)

print("List of even numbers:", x)
