# Q58: Password function with custom exception
class InvalidPasswordError(Exception):
    pass

def validate_password(password):
    if len(password) < 8:
        raise InvalidPasswordError("Password must contain at least 8 characters.")
    if not any(ch.isdigit() for ch in password):
        raise InvalidPasswordError("Password must contain at least one number.")
    return True

try:
    password = input("Enter password: ")
    validate_password(password)
    print("Password is valid.")
except InvalidPasswordError as e:
    print("Error:", e)
