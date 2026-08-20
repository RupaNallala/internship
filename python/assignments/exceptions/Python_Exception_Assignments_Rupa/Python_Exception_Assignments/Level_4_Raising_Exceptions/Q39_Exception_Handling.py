# Q39: Attendance validation
try:
    attendance = float(input("Enter attendance percentage: "))
    required = 75
    if attendance < required:
        raise ValueError("Attendance is below the required 75%.")
    print("Attendance requirement satisfied.")
except ValueError as e:
    print("Error:", e)
