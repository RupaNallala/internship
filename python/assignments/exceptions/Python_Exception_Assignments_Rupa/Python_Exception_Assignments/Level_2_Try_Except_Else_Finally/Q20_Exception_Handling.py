# Q20: Open and read a file
try:
    with open("student.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("student.txt does not exist.")
