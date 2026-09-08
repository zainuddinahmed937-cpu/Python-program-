import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = b*b - 4*a*c

if d > 0:
    print("Real and distinct roots")
    print((-b + math.sqrt(d)) / (2*a))
    print((-b - math.sqrt(d)) / (2*a))
elif d == 0:
    print("Real and equal roots")
    print(-b / (2*a))
else:
    print("Imaginary roots")
