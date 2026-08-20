# Q9: Handle AttributeError
class Student:
    def __init__(self, name):
        self.name = name

rupa = Student("Rupa")

try:
    print(rupa.phone_number)
except AttributeError:
    print("The requested attribute does not exist.")
