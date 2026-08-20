# Q30: Multiple operations with separate except blocks
try:
    number = int(input("Enter a number: "))
    index = int(input("Enter list index: "))

    names = ["Rupa", "Sweety", "Mahi", "Latha", "Sri"]
    print("Square:", number ** 2)
    print("Selected name:", names[index])
    print("Division result:", 100 / number)
except ValueError:
    print("Please enter valid integers.")
except IndexError:
    print("Invalid list index.")
except ZeroDivisionError:
    print("Number cannot be zero for division.")
