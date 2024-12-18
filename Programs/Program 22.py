x = 5
k = 0
for i in range(x, 0,-1):
    k += 1
    for j in range(1, i+1):
        print(k, end='')
    print()
