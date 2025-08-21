N = int(input("Enter N: "))
total = 0
temp = N
while temp > 0:
    total += temp % 10
    temp //= 10
print("Sum of digits =", total)
