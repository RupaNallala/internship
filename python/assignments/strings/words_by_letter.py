text = input("Enter a sentence: ")
letter = input("Enter the starting letter: ")
if "A" <= letter <= "Z":
    letter = chr(ord(letter) + 32)

matching_words = []
word = ""

for character in text + " ":
    if character != " ":
        word += character
    elif word != "":
        first_character = word[0]
        if "A" <= first_character <= "Z":
            first_character = chr(ord(first_character) + 32)
        if first_character == letter:
            matching_words.append(word)
        word = ""

print("Words beginning with", letter + ":", matching_words)
