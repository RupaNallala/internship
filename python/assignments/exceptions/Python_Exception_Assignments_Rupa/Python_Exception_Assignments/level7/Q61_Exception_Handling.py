# Q61: BankAccount class with custom exception
class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance.")
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        self.balance -= amount
        return self.balance

account = BankAccount("Rupa", 5000)

try:
    amount = float(input("Enter withdrawal amount: "))
    print("Remaining balance:", account.withdraw(amount))
except (InsufficientBalanceError, ValueError) as e:
    print("Error:", e)
