# Q63: Employee class with custom salary exception
class InvalidSalaryError(Exception):
    pass

class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError("Salary cannot be negative.")
        self.name = name
        self.salary = salary

try:
    name = input("Enter employee name: ")
    salary = float(input("Enter salary: "))
    employee = Employee(name, salary)
    print(employee.name, "salary:", employee.salary)
except (InvalidSalaryError, ValueError) as e:
    print("Error:", e)
