
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully")

    def display_books(self):
        print("Available Books:")
        for book in self.books:
            print(book)

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Book issued successfully")
        else:
            print("Book not available")

# Create object
lib = Library()

# Add books
lib.add_book("Python")
lib.add_book("Java")

# Display books
lib.display_books()

# Issue a book
lib.issue_book("Python")

# Display updated books
lib.display_books()
