# Q14: Display square using try-except-else
try:
    number = float(input("Enter a number: "))
except ValueError:
    print("Invalid number.")
else:
    print("Square:", number ** 2)
