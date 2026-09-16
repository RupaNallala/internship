# Q60: Function accepting user input with multiple exceptions
def get_result():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        return a / b
    except ValueError:
        print("Please enter integers.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    return None

result = get_result()
if result is not None:
    print("Result:", result)
