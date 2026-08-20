# Q70: Course class with invalid enrollment conditions
class InvalidEnrollmentError(Exception):
    pass

class Course:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.enrolled = 0

    def enroll(self, student_name):
        if not student_name.strip():
            raise InvalidEnrollmentError("Student name cannot be empty.")
        if self.enrolled >= self.capacity:
            raise InvalidEnrollmentError("Course is full.")
        self.enrolled += 1
        return "Enrollment successful."

course = Course("Python", 2)

try:
    student = input("Enter student name: ")
    print(course.enroll(student))
except InvalidEnrollmentError as e:
    print("Error:", e)
