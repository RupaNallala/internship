# Q45: Custom InvalidUsernameError
class InvalidUsernameError(Exception):
    pass

try:
    username = input("Enter username: ").strip()
    if not username:
        raise InvalidUsernameError("Username cannot be empty.")
    print("Username is valid.")
except InvalidUsernameError as e:
    print("Error:", e)
