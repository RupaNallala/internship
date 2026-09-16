# Q23: IndexError and ValueError
names = ["Rupa", "Sweety", "Mahi", "Latha", "Sri"]

try:
    index = int(input("Enter index: "))
    print("Name:", names[index])
except ValueError:
    print("Enter a number for the index.")
except IndexError:
    print("That index does not exist.")
