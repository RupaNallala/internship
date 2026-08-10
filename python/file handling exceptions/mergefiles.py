# Program 9
# Aim: Merge two files into a third file.

try:
    with open("file1.txt", "r") as file1:
        data1 = file1.read()

    with open("file2.txt", "r") as file2:
        data2 = file2.read()

    with open("merged.txt", "w") as merged:
        merged.write(data1)
        merged.write("\n")
        merged.write(data2)

    print("Files merged successfully.")

except FileNotFoundError:
    print("One or more files not found.")