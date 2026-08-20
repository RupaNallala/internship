# Q22: ValueError, TypeError and ZeroDivisionError
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)
except ValueError:
    print("Invalid numeric input.")
except TypeError:
    print("Invalid data type.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
