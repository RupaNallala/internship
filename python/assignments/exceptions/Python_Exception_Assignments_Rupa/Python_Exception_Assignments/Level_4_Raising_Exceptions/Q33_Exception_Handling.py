# Q33: Raise ValueError if age is below 18
try:
    age = int(input("Enter age: "))
    if age < 18:
        raise ValueError("Age must be 18 or above.")
    print("Age accepted.")
except ValueError as e:
    print("Error:", e)
