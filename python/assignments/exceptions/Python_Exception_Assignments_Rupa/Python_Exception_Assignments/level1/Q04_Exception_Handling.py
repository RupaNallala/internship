# Q4: Handle KeyError
students = {"Rupa": 85, "Sweety": 90, "Mahi": 78, "Latha": 88, "Sri": 92}

try:
    name = input("Enter student name: ")
    print("Marks:", students[name])
except KeyError:
    print("Student name not found.")
