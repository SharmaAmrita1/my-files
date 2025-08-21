a, b, c = map(int, input("Enter 3 numbers: ").split())
if a >= b and a >= c:
    print("Maximum =", a)
elif b >= a and b >= c:
    print("Maximum =", b)
else:
    print("Maximum =", c)
