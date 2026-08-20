# Q73: Library Management System
class BookError(Exception):
    pass

books = {"B101": "Python", "B102": "SQL"}
issued = set()

try:
    book_id = input("Enter book ID: ")
    if book_id in issued:
        raise BookError("Book is unavailable.")
    if book_id not in books:
        raise BookError("Invalid book ID.")
    issued.add(book_id)
    print("Book issued:", books[book_id])
except BookError as e:
    print("Error:", e)
