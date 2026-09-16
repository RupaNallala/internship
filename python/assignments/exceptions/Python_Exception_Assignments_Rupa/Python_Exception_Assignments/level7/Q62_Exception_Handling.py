# Q62: Student class with custom marks exception
class InvalidMarksError(Exception):
    pass

class Student:
    def __init__(self, name, marks):
        if marks < 0 or marks > 100:
            raise InvalidMarksError("Marks must be between 0 and 100.")
        self.name = name
        self.marks = marks

try:
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    student = Student(name, marks)
    print(student.name, "has", student.marks, "marks.")
except (InvalidMarksError, ValueError) as e:
    print("Error:", e)
