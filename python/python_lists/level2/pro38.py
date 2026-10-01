#Insert an element after every occurrence of a particular value.
numbers = [1, 2, 3, 2, 4, 2]
target = 2
new_value = 99
result = []
for number in numbers:
    result.append(number)
    if number == target:
        result.append(new_value)
print(result)
