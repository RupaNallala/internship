#Replace all occurrences of one value with another.
numbers = [1, 2, 2, 3, 2, 4]
old_value = 2
new_value = 99
for i in range(len(numbers)):
    if numbers[i] == old_value:
        numbers[i] = new_value
print(numbers)
