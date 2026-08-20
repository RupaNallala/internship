# Program 3
# Aim: Append a new course to an existing file.

try:
    with open("student.txt", "a") as file:
        file.write("New Course : Python Programming\n")

    print("Data appended successfully.")

except Exception as e:
    print("Error:", e)