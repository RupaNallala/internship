# Q80: Menu-Driven Exception Handling Application
class InvalidAmountError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

balance = 5000

while True:
    print("\n--- Exception Handling Menu ---")
    print("1. Divide numbers")
    print("2. Withdraw money")
    print("3. Validate password")
    print("4. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", a / b)

        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            if amount <= 0:
                raise InvalidAmountError("Amount must be positive.")
            if amount > balance:
                raise InsufficientBalanceError("Insufficient balance.")
            balance -= amount
            print("Withdrawal successful.")
            print("Balance:", balance)

        elif choice == "3":
            password = input("Enter password: ")
            if len(password) < 8:
                raise ValueError("Password must have at least 8 characters.")
            print("Password accepted.")

        elif choice == "4":
            print("Thank you, Rupa!")
            break

        else:
            raise ValueError("Invalid menu choice.")

    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except ValueError as e:
        print("Value error:", e)
    except (InvalidAmountError, InsufficientBalanceError) as e:
        print("Transaction error:", e)
    else:
        print("Operation completed successfully.")
    finally:
        print("Operation finished.")
