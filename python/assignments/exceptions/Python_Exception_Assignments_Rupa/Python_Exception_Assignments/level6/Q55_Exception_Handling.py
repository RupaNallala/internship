# Q55: Function to search dictionary key
def get_marks(marks, name):
    try:
        return marks[name]
    except KeyError:
        return None

marks = {"Rupa": 90, "Sweety": 85, "Mahi": 95, "Latha": 88, "Sri": 92}

name = input("Enter student name: ")

result = get_marks(marks, name)
if result is None:
    print("Student not found.")
else:
    print("Marks:", result)
