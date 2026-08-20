# Q71: Banking System
class InvalidAmountError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

class InvalidAccountError(Exception):
    pass

accounts = {"1001": 5000, "1002": 3000}

try:
    account = input("Enter account number: ")
    if account not in accounts:
        raise InvalidAccountError("Invalid account number.")

    amount = float(input("Enter withdrawal amount: "))
    if amount <= 0:
        raise InvalidAmountError("Amount must be positive.")
    if amount > accounts[account]:
        raise InsufficientBalanceError("Insufficient balance.")

    accounts[account] -= amount
    print("Withdrawal successful.")
    print("Balance:", accounts[account])
except (InvalidAmountError, InsufficientBalanceError, InvalidAccountError) as e:
    print("Error:", e)
except ValueError:
    print("Enter a valid amount.")
