try:
    balance = 5000

    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise Exception("Withdrawal amount must be greater than zero.")

    if amount > balance:
        raise Exception("Insufficient balance.")

    balance = balance - amount

    print("Withdrawal Successful")
    print("Remaining Balance:", balance)

except Exception as e:
    print(e)