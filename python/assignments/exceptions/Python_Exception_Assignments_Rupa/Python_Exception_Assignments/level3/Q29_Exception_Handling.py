# Q29: Read numbers from a file and handle errors
filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        total = 0
        for line in file:
            number = float(line.strip())
            total += number
        print("Total:", total)
except FileNotFoundError:
    print("File not found.")
except ValueError:
    print("The file contains invalid numeric data.")
except PermissionError:
    print("Permission denied.")
