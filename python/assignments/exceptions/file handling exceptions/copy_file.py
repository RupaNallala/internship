# Program 8
# Aim: Copy one text file to another.

try:
    with open("source.txt", "r") as source:
        data = source.read()

    with open("destination.txt", "w") as destination:
        destination.write(data)

    print("File copied successfully.")

except FileNotFoundError:
    print("Source file not found.")