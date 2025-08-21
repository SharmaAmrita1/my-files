A, B, C = map(int, input("Enter 3 numbers: ").split())
if A <= B and A <= C:
    print("Minimum =", A)
elif B <= A and B <= C:
    print("Minimum =", B)
else:
    print("Minimum =", C)
