data = (
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
)

print("Before modification:")
print(data)

# Accessing elements
print("First list:", data[0])
print("First element of first list:", data[0][0])

# Modifying elements inside the lists
data[0][0] = 100
data[1].append(70)

print("After modification:")
print(data)