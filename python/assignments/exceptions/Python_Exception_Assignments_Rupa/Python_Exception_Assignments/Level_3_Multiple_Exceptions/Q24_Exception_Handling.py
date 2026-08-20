# Q24: KeyError and TypeError with dictionary
marks = {"Rupa": 95, "Sweety": 88, "Mahi": 91}

try:
    key = input("Enter student name: ")
    print("Marks:", marks[key])
except KeyError:
    print("Student not found.")
except TypeError:
    print("Invalid key type.")
