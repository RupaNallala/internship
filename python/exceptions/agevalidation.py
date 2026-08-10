try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

    if age > 100:
        raise ValueError("Age cannot be above 100.")

    print("Valid Age")

except ValueError as e:
    print(e)