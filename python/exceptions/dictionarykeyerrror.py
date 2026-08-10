try:
    employee = {
        "id": 101,
        "name": "Ravi",
        "salary": 30000,
        "department": "IT"
    }

    key = input("Enter the key: ")

    print("Value:", employee[key])

except KeyError:
    print("Key not found in the dictionary.")