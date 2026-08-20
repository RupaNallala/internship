# Q40: Employee salary validation
try:
    salary = float(input("Enter salary: "))
    if salary < 0:
        raise ValueError("Salary cannot be negative.")
    print("Valid salary:", salary)
except ValueError as e:
    print("Error:", e)
