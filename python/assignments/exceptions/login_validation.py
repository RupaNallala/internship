try:
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username != "admin":
        raise Exception("Invalid Username.")

    if password != "1234":
        raise Exception("Invalid Password.")

    print("Login Successful")

except Exception as e:
    print(e)