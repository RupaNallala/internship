# Q43: Custom InvalidMarksError
class InvalidMarksError(Exception):
    pass

try:
    marks = float(input("Enter marks: "))
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100.")
    print("Valid marks.")
except InvalidMarksError as e:
    print("Error:", e)
except ValueError:
    print("Enter valid marks.")
