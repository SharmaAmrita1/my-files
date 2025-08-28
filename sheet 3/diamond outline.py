n = int(input("Enter number of rows: "))
for i in range(n):
    print("*" * (n-i) + " " * (2*i) + "*" * (n-i))
for i in range(n):
    print("*" * (i+1) + " " * (2*(n-i-1)) + "*" * (i+1))
