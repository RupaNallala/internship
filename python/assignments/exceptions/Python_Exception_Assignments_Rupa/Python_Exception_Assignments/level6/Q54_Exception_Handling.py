# Q54: Function to access list element
def get_name(names, index):
    try:
        return names[index]
    except IndexError:
        return None

names = ["Rupa", "Sweety", "Mahi", "Latha", "Sri"]

try:
    index = int(input("Enter index: "))
    name = get_name(names, index)
    if name is None:
        print("Index out of range.")
    else:
        print("Name:", name)
except ValueError:
    print("Enter an integer index.")
