# Q66: LoginSystem with custom exceptions
class InvalidUsernameError(Exception):
    pass

class InvalidPasswordError(Exception):
    pass

class LoginSystem:
    def __init__(self):
        self.users = {"Rupa": "Rupa1234", "Sweety": "Sweety1234"}

    def login(self, username, password):
        if username not in self.users:
            raise InvalidUsernameError("Username not found.")
        if self.users[username] != password:
            raise InvalidPasswordError("Incorrect password.")
        return "Login successful."

system = LoginSystem()

try:
    username = input("Username: ")
    password = input("Password: ")
    print(system.login(username, password))
except (InvalidUsernameError, InvalidPasswordError) as e:
    print("Error:", e)
