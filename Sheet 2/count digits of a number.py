N = int(input("Enter N: "))
count = 0
temp = N
while temp > 0:
    count += 1
    temp //= 10
print("Count of digits =", count)
