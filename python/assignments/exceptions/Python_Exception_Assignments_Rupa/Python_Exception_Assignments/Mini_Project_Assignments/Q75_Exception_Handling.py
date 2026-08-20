# Q75: Employee Management System
class EmployeeError(Exception):
    pass

employees = {}

try:
    employee_id = input("Enter employee ID: ")
    if employee_id in employees:
        raise EmployeeError("Employee ID already exists.")

    name = input("Enter employee name: ")
    salary = float(input("Enter salary: "))
    department = input("Enter department: ")

    if salary < 0:
        raise EmployeeError("Salary cannot be negative.")
    if not department.strip():
        raise EmployeeError("Department cannot be empty.")

    employees[employee_id] = {
        "name": name,
        "salary": salary,
        "department": department
    }
    print("Employee added successfully.")
except EmployeeError as e:
    print("Error:", e)
except ValueError:
    print("Enter a valid salary.")
