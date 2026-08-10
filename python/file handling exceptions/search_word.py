# Program 7
# Aim: Search for a word in a file.

try:
    word = input("Enter word to search: ")

    with open("article.txt", "r") as file:
        content = file.read()

    if word.lower() in content.lower():
        print("Word Found.")
    else:
        print("Word Not Found.")

except FileNotFoundError:
    print("File not found.")