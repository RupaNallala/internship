# Q17: Four arithmetic operations with exception handling
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
