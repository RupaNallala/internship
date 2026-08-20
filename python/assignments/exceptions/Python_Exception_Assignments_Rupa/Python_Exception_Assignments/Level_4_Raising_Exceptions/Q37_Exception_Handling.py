# Q37: Username validation
try:
    username = input("Enter username: ").strip()
    if username == "":
        raise ValueError("Username cannot be empty.")
    print("Username accepted:", username)
except ValueError as e:
    print("Error:", e)
