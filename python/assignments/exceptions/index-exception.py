try:
    subjects = ["English", "Mathematics", "Physics", "Chemistry", "Computer Science"]

    index = int(input("Enter the index : "))

     

except ValueError:
    print(" Please enter an integer.")

except IndexError:
    print("  Please enter a number between 0 and 4.")