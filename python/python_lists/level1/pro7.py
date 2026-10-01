#Count how many times a given number occurs in a list.
numbers = [2, 5, 2, 8, 2, 9]
target = 2
count = 0
for number in numbers:
    if number == target:
        count += 1
print("Count:", count)
print("count:",numbers.count(target))
