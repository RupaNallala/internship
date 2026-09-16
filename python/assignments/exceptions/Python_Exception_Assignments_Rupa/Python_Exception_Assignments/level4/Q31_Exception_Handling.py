# Q31: Raise ValueError for negative number
try:
    number = float(input("Enter a number: "))
    if number < 0:
        raise ValueError("Negative numbers are not allowed.")
    print("Accepted number:", number)
except ValueError as e:
    print("Error:", e)
