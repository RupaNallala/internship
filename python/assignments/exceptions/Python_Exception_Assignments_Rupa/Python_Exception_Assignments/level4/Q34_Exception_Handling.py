# Q34: Raise exception for insufficient balance
balance = 5000

try:
    amount = float(input("Enter withdrawal amount: "))
    if amount > balance:
        raise ValueError("Withdrawal amount is greater than available balance.")
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive.")
    print("Withdrawal successful.")
except ValueError as e:
    print("Error:", e)
