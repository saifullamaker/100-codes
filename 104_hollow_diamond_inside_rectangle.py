n = 5
for i in range(n):
    for j in range(2 * n - 1):
        d = abs(n - 1 - j)
        if i == n - 1 or i == d:
            print("*", end="")
        else:
            print(" ", end="")
    print()
