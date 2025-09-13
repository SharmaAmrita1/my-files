A = [1, 591]
B = 5

found = 0

for num in A:
    if str(B) in str(num):
        found = 1
        break

print(found)  # Output: 1
