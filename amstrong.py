n = int(input("Enter a 3-digit number: "))

a = n // 100
b = (n // 10) % 10
c = n % 10

if a**3 + b**3 + c**3 == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
