# Q32: Validate student marks
try:
    marks = float(input("Enter marks: "))
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")
    print("Valid marks:", marks)
except ValueError as e:
    print("Error:", e)
