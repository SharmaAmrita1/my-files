A = [1,2,3,44,]
B= 3
result = []
for num in A:
    for digit in str(num):
        result.append(int(digit) +B )
print(result)