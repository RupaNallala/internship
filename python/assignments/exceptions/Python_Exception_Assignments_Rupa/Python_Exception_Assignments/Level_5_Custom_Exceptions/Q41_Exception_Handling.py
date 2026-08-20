# Q41: Custom InvalidAgeError
class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")
    print("Age is valid.")
except InvalidAgeError as e:
    print("Error:", e)
except ValueError:
    print("Enter a valid age.")
