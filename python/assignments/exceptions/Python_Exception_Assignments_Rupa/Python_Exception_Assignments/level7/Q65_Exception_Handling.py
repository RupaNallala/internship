# Q65: Library class with unavailable books
class BookNotAvailableError(Exception):
    pass

class Library:
    def __init__(self):
        self.books = {"Python": True, "SQL": True, "Java": False}

    def issue_book(self, book):
        if book not in self.books:
            raise BookNotAvailableError("Book not found.")
        if not self.books[book]:
            raise BookNotAvailableError("Book is unavailable.")
        self.books[book] = False
        return "Book issued successfully."

library = Library()

try:
    book = input("Enter book name: ")
    print(library.issue_book(book))
except BookNotAvailableError as e:
    print("Error:", e)
