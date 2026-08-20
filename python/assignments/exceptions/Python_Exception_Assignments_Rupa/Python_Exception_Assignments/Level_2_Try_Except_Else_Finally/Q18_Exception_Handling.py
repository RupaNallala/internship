# Q18: List element using user input
names = ["Rupa", "Sweety", "Mahi", "Latha", "Sri"]

try:
    index = int(input("Enter index: "))
    print("Selected name:", names[index])
except ValueError:
    print("Index must be an integer.")
except IndexError:
    print("Index is outside the list.")
