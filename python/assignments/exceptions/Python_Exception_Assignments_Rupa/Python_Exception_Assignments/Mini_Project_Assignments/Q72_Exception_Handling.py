# Q72: Student Management System
class DuplicateStudentError(Exception):
    pass

class StudentNotFoundError(Exception):
    pass

class InvalidMarksError(Exception):
    pass

students = {}

def add_student(student_id, name, marks):
    if student_id in students:
        raise DuplicateStudentError("Student ID already exists.")
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100.")
    students[student_id] = {"name": name, "marks": marks}

def find_student(student_id):
    if student_id not in students:
        raise StudentNotFoundError("Student not found.")
    return students[student_id]

try:
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    add_student(student_id, name, marks)
    print("Student added.")

    search_id = input("Enter ID to search: ")
    print(find_student(search_id))
except (DuplicateStudentError, StudentNotFoundError, InvalidMarksError) as e:
    print("Error:", e)
except ValueError:
    print("Enter valid marks.")
