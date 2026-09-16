# Q69: Hospital class with invalid patient information
class InvalidPatientError(Exception):
    pass

class Hospital:
    def register_patient(self, name, age):
        if not name.strip():
            raise InvalidPatientError("Patient name cannot be empty.")
        if age <= 0:
            raise InvalidPatientError("Patient age must be positive.")
        return "Patient registered successfully."

hospital = Hospital()

try:
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    print(hospital.register_patient(name, age))
except InvalidPatientError as e:
    print("Error:", e)
except ValueError:
    print("Enter a valid age.")
