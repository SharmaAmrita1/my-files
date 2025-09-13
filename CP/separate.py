A = [12345]

odd_digits = ""
even_digits = ""

for num in A:
    for digit in str(num):
        if int(digit) % 2 == 0:
            even_digits += digit
        else:
            odd_digits += digit

print(odd_digits)
print(even_digits)
