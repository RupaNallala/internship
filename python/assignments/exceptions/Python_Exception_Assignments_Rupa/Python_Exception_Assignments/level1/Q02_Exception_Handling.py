# Q2: Handle invalid numeric input
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Sum:", a + b)
except ValueError:
    print("Invalid input. Please enter numbers only.")
