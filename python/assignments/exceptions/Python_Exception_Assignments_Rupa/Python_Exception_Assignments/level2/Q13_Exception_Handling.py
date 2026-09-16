# Q13: Read a file using try-except-else-finally
file = None

try:
    file = open("student.txt", "r")
except FileNotFoundError:
    print("File does not exist.")
else:
    print("File content:")
    print(file.read())
finally:
    if file:
        file.close()
    print("File operation completed.")
