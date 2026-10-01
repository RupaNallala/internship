#Count positive, negative, and zero values.
numbers = [10, -5, 0, 20, -2, 0, 8]
positive = 0
negative = 0
zero = 0
for number in numbers:
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        zero += 1

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)
