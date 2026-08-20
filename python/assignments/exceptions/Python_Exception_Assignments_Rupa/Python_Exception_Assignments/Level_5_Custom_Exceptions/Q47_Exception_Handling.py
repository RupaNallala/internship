# Q47: Custom InvalidSalaryError
class InvalidSalaryError(Exception):
    pass

try:
    salary = float(input("Enter salary: "))
    if salary < 0:
        raise InvalidSalaryError("Salary cannot be negative.")
    print("Valid salary:", salary)
except InvalidSalaryError as e:
    print("Error:", e)
except ValueError:
    print("Enter a valid salary.")
