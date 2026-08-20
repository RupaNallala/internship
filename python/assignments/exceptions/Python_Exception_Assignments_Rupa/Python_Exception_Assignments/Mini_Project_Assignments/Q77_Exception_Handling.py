# Q77: ATM System
class ATMError(Exception):
    pass

accounts = {"1001": {"pin": "1234", "balance": 10000}}

try:
    account = input("Enter account number: ")
    if account not in accounts:
        raise ATMError("Invalid account.")

    pin = input("Enter PIN: ")
    if pin != accounts[account]["pin"]:
        raise ATMError("Invalid PIN.")

    amount = float(input("Enter withdrawal amount: "))
    if amount <= 0:
        raise ATMError("Invalid withdrawal amount.")
    if amount > accounts[account]["balance"]:
        raise ATMError("Insufficient balance.")

    accounts[account]["balance"] -= amount
    print("Withdrawal successful.")
    print("Balance:", accounts[account]["balance"])
except ATMError as e:
    print("Error:", e)
except ValueError:
    print("Enter a valid amount.")
