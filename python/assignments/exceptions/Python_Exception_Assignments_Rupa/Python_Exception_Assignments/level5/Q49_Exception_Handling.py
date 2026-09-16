# Q49: Custom BookNotAvailableError
class BookNotAvailableError(Exception):
    pass

books = {"Python": True, "SQL": True, "HTML": False}

try:
    book = input("Enter book name: ")
    if book not in books:
        raise BookNotAvailableError("Book does not exist.")
    if not books[book]:
        raise BookNotAvailableError("Book is currently unavailable.")
    print("Book is available.")
except BookNotAvailableError as e:
    print("Error:", e)
