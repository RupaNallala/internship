# Program 5
# Aim: Count the number of lines in a file.

try:
    with open("student.txt", "r") as file:
        lines = file.readlines()

    print("Total Lines :", len(lines))

except FileNotFoundError:
    print("File not found.")