x = 0
for day in range(1,8):
    y = float(input("Enter temperature for a day {}: ".format(day)))
    x += y

z = x/7
print("Average temperature of all seven days are: ", z)
