# Q53: Function to withdraw money
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive.")
    if amount > balance:
        raise ValueError("Insufficient balance.")
    return balance - amount

try:
    balance = 5000
    amount = float(input("Enter withdrawal amount: "))
    balance = withdraw(balance, amount)
    print("Remaining balance:", balance)
except ValueError as e:
    print("Error:", e)
