# Q11: try, except and else
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a / b
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid number.")
else:
    print("Division result:", result)
