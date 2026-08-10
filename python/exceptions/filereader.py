try:
    filename = input("Enter filename: ")

    file = open(filename, "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("File not found.")