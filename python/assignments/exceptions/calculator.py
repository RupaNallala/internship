try:
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    op = input("Enter Operator (+,-,*,/): ")

    if op == "+":
        result = num1 + num2

    elif op == "-":
        result = num1 - num2

    elif op == "*":
        result = num1 * num2

    elif op == "/":
        result = num1 / num2

    else:
        raise ValueError("Invalid Operator")

except ValueError as e:
    print(e)

except ZeroDivisionError:
    print("Division by zero is not allowed.")

else:
    print("Result =", result)

finally:
    print("Calculator Program Ended")