students = [
    ("Rahul", 80),
    ("Teja", 90),
    ("Suresh", 75),
    ("Kiran", 85)
]

search_name = input("Enter student name: ")

found = False

for student in students:
    if student[0].lower() == search_name.lower():
        print("Student found!")
        print("Name:", student[0])
        print("Marks:", student[1])
        found = True
        break

if not found:
    print("Student not found.")