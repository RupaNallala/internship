text = input("Enter a string: ")

words = text.split()
result = ""

for word in words:
    result += word[0].upper() + word[1:] + " "

print(result.strip())