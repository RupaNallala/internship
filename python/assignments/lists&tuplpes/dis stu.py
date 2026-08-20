students = [
    ("Rahul", 80),
    ("Teja", 70),
    ("Suresh", 90),
    ("Kiran", 65),
    ("Anil", 85)
]

print("Students who scored above 75:")

for name, marks in students:
    if marks > 75:
        print(name, "-", marks)
