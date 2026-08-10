try:
    print("===== Student Registration Form =====")

    name = input("Enter Student Name: ")

    age = int(input("Enter Age: "))
    if age < 16 or age > 30:
        raise ValueError("Age must be between 16 and 30.")

    roll_no = int(input("Enter Roll Number: "))

    email = input("Enter Email: ")
    if "@" not in email or "." not in email:
        raise ValueError("Invalid Email Address.")

    mobile = input("Enter Mobile Number: ")
    if len(mobile) != 10 or not mobile.isdigit():
        raise ValueError("Mobile number must contain exactly 10 digits.")

    print("\n===== Registration Successful =====")
    print("Name      :", name)
    print("Age       :", age)
    print("Roll No   :", roll_no)
    print("Email     :", email)
    print("Mobile    :", mobile)

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Unexpected Error:", e)