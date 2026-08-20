 text = input("Enter a string: ")

unique = True

for ch in text:
    if text.count(ch) > 1:
        unique = False
        break

if unique:
    print("All characters are unique")
else:
    print("Characters are not unique")