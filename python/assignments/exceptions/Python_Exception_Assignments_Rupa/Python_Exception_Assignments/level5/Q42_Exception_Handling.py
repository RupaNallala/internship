# Q42: Custom InsufficientBalanceError
class InsufficientBalanceError(Exception):
    pass

balance = 5000

try:
    amount = float(input("Enter withdrawal amount: "))
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance.")
    print("Withdrawal successful.")
except InsufficientBalanceError as e:
    print("Error:", e)
except ValueError:
    print("Enter a valid amount.")
