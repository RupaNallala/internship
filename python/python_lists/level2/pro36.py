#Remove all occurrences of a particular number.
numbers = [2, 5, 2, 8, 2, 9]
target = 2
new_list = []
for number in numbers:
    if number != target:
        new_list.append(number)
print(new_list)
