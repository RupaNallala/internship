# Q28: Dictionary key with invalid input and missing key
marks = {"Rupa": 90, "Sweety": 85, "Mahi": 95, "Latha": 88, "Sri": 92}

try:
    key = input("Enter student name: ").strip()
    if not key:
        raise ValueError("Student name cannot be empty.")
    print("Marks:", marks[key])
except ValueError as e:
    print("Invalid input:", e)
except KeyError:
    print("Student name not found.")
