temp = float(input("Enter temperature: "))
choice = input("Enter C or F: ")

if choice == "C":
    print("Fahrenheit =", (temp * 9/5) + 32)
else:
    print("Celsius =", (temp - 32) * 5/9)
