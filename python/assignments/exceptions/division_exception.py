try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2

    print("Division =", result)

except ValueError:
    print(" Please enter only numbers.")

except ZeroDivisionError:
    print(" Division by zero is not allowed.")