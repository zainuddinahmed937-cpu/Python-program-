balance = float(input("Enter balance: "))
amount = float(input("Enter withdrawal amount: "))
minimum = 500

if amount <= balance and balance - amount >= minimum:
    print("Withdrawal approved")
else:
    print("Withdrawal rejected")
