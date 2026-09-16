# Q48: Custom InvalidEmailError
class InvalidEmailError(Exception):
    pass

try:
    email = input("Enter email: ").strip()
    if "@" not in email or "." not in email.split("@")[-1]:
        raise InvalidEmailError("Invalid email address.")
    print("Email is valid.")
except InvalidEmailError as e:
    print("Error:", e)
