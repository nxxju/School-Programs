x = int(input("Enter a number: "))
y = x
z = 0
while(x > 0):
    dig = x%10
    z = z*10+dig
    x=x//10
if(y == z):
    print("The number is palindrome.")
else:
    print("The number is not palindrome.")
