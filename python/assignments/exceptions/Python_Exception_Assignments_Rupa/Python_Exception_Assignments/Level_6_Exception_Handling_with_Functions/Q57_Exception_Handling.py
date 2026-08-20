# Q57: Function to calculate student grade
def calculate_grade(marks):
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")

    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

try:
    marks = float(input("Enter marks: "))
    print("Grade:", calculate_grade(marks))
except ValueError as e:
    print("Error:", e)
