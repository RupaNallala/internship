students = [
    ["Rahul", 80, 75, 90],
    ["Teja", 85, 90, 88],
    ["Suresh", 70, 65, 75],
    ["Kiran", 95, 92, 90]
]

for student in students:
    name = student[0]
    
    mark1 = student[1]
    mark2 = student[2]
    mark3 = student[3]
    
    total = mark1 + mark2 + mark3
    average = total / 3
    
    print("Name:", name)
    print("Total:", total)
    print("Average:", average)
    print("--------------------")