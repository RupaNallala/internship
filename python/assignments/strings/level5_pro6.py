#Write a program to find the largest word in a sentence.
str="java is a programming language"
words = str.split()
largest = words[0]

for word in words:
    if len(word) > len(largest):
        largest = word

print("Largest word:", largest)
