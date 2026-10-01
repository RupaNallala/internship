#Copy one list into another list without using copy().
numbers = [10, 20, 30, 40]
new_list = []
for number in numbers:
    new_list.append(number)
print("Original:", numbers)
print("Copied:", new_list)
