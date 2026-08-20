text = input("Enter a string: ")

result = ""

for ch in text:
    if ch.isalnum() or ch.isspace():
        result += ch

print(result)