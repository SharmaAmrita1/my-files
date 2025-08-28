n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(n):
        if j == i or j == 0 or i == 0 or i == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
