# Q76: Login and Registration System
class UsernameError(Exception):
    pass

class PasswordError(Exception):
    pass

class DuplicateUsernameError(Exception):
    pass

class InvalidLoginError(Exception):
    pass

users = {}

def register(username, password):
    if not username.strip():
        raise UsernameError("Username cannot be empty.")
    if username in users:
        raise DuplicateUsernameError("Username already exists.")
    if len(password) < 8:
        raise PasswordError("Password must have at least 8 characters.")
    users[username] = password

def login(username, password):
    if username not in users or users[username] != password:
        raise InvalidLoginError("Invalid username or password.")

try:
    username = input("Create username: ")
    password = input("Create password: ")
    register(username, password)
    print("Registration successful.")

    username = input("Login username: ")
    password = input("Login password: ")
    login(username, password)
    print("Login successful.")
except (UsernameError, PasswordError, DuplicateUsernameError, InvalidLoginError) as e:
    print("Error:", e)
