#Find the largest number in a list without using max().
num = [12, 45, 7, 89, 34]
largest = num[0]
for number in num:
    if number > largest:
        largest = number
print("Largest:", largest)
