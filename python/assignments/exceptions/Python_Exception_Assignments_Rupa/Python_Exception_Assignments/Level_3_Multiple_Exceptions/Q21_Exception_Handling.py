# Q21: ValueError and ZeroDivisionError
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print("Result:", a / b)
except ValueError:
    print("Please enter integers only.")
except ZeroDivisionError:
    print("Denominator cannot be zero.")
