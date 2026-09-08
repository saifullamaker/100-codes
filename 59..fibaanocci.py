terms = int(input("How many terms? "))

a, b = 0, 1

for _ in range(terms):
    print(a, end=" ")
    a, b = b, a + b
