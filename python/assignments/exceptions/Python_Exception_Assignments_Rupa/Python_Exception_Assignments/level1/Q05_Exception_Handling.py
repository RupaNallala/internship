# Q5: Handle ValueError while converting string to integer
text = input("Enter a number: ")

try:
    number = int(text)
    print("Integer:", number)
except ValueError:
    print("The entered value is not a valid integer.")
