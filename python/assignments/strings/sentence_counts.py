sentence = input("Enter a sentence: ")

vowels = "aeiouAEIOU"
word_count = 0
character_count = 0
digit_count = 0
vowel_count = 0
space_count = 0
inside_word = False

for character in sentence:
    character_count += 1
    if "0" <= character <= "9":
        digit_count += 1
    if character in vowels:
        vowel_count += 1
    if character == " ":
        space_count += 1
        inside_word = False
    elif not inside_word:
        word_count += 1
        inside_word = True

print("Words:", word_count)
print("Characters:", character_count)
print("Digits:", digit_count)
print("Vowels:", vowel_count)
print("Spaces:", space_count)
