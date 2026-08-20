# Q50: Custom InvalidTransactionError
class InvalidTransactionError(Exception):
    pass

try:
    amount = float(input("Enter transaction amount: "))
    if amount <= 0:
        raise InvalidTransactionError("Transaction amount must be positive.")
    print("Transaction accepted.")
except InvalidTransactionError as e:
    print("Error:", e)
except ValueError:
    print("Enter a valid amount.")
