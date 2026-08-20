# Program 4
# Aim: Read a file line by line.

try:
    with open("student.txt", "r") as file:
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("File not found.")