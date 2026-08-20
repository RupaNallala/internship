# Q12: try, except and finally
try:
    number = int(input("Enter a number: "))
    print("Number:", number)
except ValueError:
    print("Invalid number.")
finally:
    print("Finally block always executes.")
