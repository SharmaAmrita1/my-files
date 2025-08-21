perc = int(input("Enter percentage: "))
if perc < 25:
    print("Grade: D")
elif perc <= 45:
    print("Grade: C")
elif perc <= 65:
    print("Grade: B")
elif perc <= 85:
    print("Grade: A")
else:
    print("Grade: A+")
