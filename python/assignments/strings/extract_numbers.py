 text = input("Enter a string: ")

numbers = ""

for ch in text:
    if ch.isdigit():
        numbers += ch

print("Numbers:", numbers)