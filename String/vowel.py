T = int(input("enter how many"))
ch = "AEIOUaeiou"
vowel  = 0
consonant = 0

for _ in range(T):
    n = input()
    for i in n:
        if i in ch:
            vowel += 1
        else:
            consonant += 1
print(vowel, consonant)
