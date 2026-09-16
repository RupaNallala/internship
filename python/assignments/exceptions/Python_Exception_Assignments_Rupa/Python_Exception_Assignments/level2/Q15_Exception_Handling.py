# Q15: Bank withdrawal using try-except-finally
balance = 5000

try:
    amount = float(input("Enter withdrawal amount: "))
    if amount <= 0:
        raise ValueError("Amount must be positive.")
    if amount > balance:
        raise ValueError("Insufficient balance.")
    balance -= amount
    print("Withdrawal successful.")
    print("Remaining balance:", balance)
except ValueError as e:
    print("Transaction failed:", e)
finally:
    print("Thank you, Rupa. Please take your receipt.")
