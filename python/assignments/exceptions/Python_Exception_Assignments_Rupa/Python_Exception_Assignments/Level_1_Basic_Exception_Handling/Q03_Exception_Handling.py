# Q3: Handle IndexError
friends = ["Rupa", "Sweety", "Mahi", "Latha", "Sri"]

try:
    index = int(input("Enter list index: "))
    print("Name:", friends[index])
except IndexError:
    print("Invalid index.")
except ValueError:
    print("Enter a valid integer index.")
