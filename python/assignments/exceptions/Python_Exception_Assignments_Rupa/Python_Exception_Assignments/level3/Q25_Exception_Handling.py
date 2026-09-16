# Q25: FileNotFoundError and PermissionError
filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File was not found.")
except PermissionError:
    print("You do not have permission to open this file.")
