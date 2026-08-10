# Program 6
# Aim: Count the number of words and characters in a file.

try:
    with open("article.txt", "r") as file:
        content = file.read()

    words = len(content.split())
    characters = len(content)

    print("Total Words      :", words)
    print("Total Characters :", characters)

except FileNotFoundError:
    print("File not found.")