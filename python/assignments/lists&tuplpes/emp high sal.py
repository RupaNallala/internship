employees = [
    ("Rahul", "Manager", 60000),
    ("Teja", "Developer", 50000),
    ("Suresh", "Designer", 45000),
    ("Kiran", "Developer", 55000)
]

highest_employee = employees[0]

for employee in employees:
    if employee[2] > highest_employee[2]:
        highest_employee = employee

print("Employee with highest salary:")
print("Name:", highest_employee[0])
print("Designation:", highest_employee[1])
print("Salary:", highest_employee[2])