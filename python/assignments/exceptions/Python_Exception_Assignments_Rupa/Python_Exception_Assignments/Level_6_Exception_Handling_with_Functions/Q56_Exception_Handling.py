# Q56: Function to read a file
def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return None
    except PermissionError:
        print("Permission denied.")
        return None

filename = input("Enter file name: ")
content = read_file(filename)

if content is None:
    print("Unable to read the file.")
else:
    print(content)
