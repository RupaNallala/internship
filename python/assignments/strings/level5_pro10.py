sentence = input("Enter a sentence: ")

words = sentence.split()

result = ""

for word in words[::-1]:
    result += word + " "

print("Reversed sentence:", result)