# Q19: Dictionary value using user input
marks = {"Rupa": 91, "Sweety": 86, "Mahi": 94, "Latha": 89, "Sri": 90}

try:
    name = input("Enter student name: ")
    print("Marks:", marks[name])
except KeyError:
    print("No marks found for that student.")
