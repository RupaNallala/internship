# Q79: File Management System
class FileDataError(Exception):
    pass

filename = input("Enter file name: ")

try:
    if not filename.endswith(".txt"):
        raise FileDataError("Only .txt files are accepted.")

    with open(filename, "r") as file:
        content = file.read()

    if not content.strip():
        raise FileDataError("File contains no data.")

    print("File read successfully.")
    print(content)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
except FileDataError as e:
    print("Error:", e)
