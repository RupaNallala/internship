# Program 10
# Aim: Replace a word in a file.

try:
    with open("article.txt", "r") as file:
        content = file.read()

    old_word = input("Enter old word: ")
    new_word = input("Enter new word: ")

    updated_content = content.replace(old_word, new_word)

    with open("article.txt", "w") as file:
        file.write(updated_content)

    print("Word replaced successfully.")

except FileNotFoundError:
    print("File not found.")