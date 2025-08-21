A = int(input("Enter A: "))
original = A
rev = 0
while A > 0:
    rev = rev * 10 + A % 10
    A //= 10

if original == rev:
    print("Yes, Palindrome")
else:
    print("No, Not a Palindrome")
