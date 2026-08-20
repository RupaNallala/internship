class InvalidSalaryError(Exception):
    pass

try:
    salary = int(input("Enter Salary: "))

    if salary < 10000:
        raise InvalidSalaryError("Salary must be at least ₹10,000.")

    print("Valid Salary")

except InvalidSalaryError as e:
    print(e)