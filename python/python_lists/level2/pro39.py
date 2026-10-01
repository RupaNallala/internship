#Find the frequency of every element in a list using simple logic.
numbers = [1, 2, 2, 3, 1, 2, 4]
frequency = {}
for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1
for number in frequency:
    print(number, ":", frequency[number])

