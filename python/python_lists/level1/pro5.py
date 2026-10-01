#Find the smallest number in a list without using min().
num = [12, 45, 7, 89, 34]
smallest = num[0]
for number in num:
    if number < smallest:
        smallest = number
print("Smallest:", smallest)
