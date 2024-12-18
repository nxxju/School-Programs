x = int(input("Enter a number: "))
y = 0
z = x

while z > 0:
    d = z % 10
    y += d ** 3
    z //= 10
if x == y:
    print(x, "is an Armstrong Number")
else:
    print(x, "is not an Armstrong Number")
