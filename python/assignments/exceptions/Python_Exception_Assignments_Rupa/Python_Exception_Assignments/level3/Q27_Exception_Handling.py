# Q27: List index and possible errors
names = ["Rupa", "Sweety", "Mahi", "Latha", "Sri"]

try:
    index = int(input("Enter index: "))
    print("Name:", names[index])
except ValueError:
    print("Index must be an integer.")
except IndexError:
    print("Index is out of range.")
except TypeError:
    print("Invalid index type.")
except Exception as e:
    print("Unexpected error:", e)
