#Find the average of numbers in a list.
numbers = [10, 20, 30, 40, 50]
num=[1,2,3,4,5]
total = 0
count = 0
for number in numbers:
    total += number
    count += 1
average = total / count
print("Average:", average)
avg=sum(num)/len(num)
print("Average:",avg)
