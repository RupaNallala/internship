# Q51: Function to divide two numbers
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = divide(a, b)
    if result is not None:
        print("Result:", result)
except ValueError:
    print("Enter valid numbers.")
