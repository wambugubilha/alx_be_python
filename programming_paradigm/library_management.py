class Book:
    def __init__(self, title, author):
        self.title = title               # Public attribute
        self.author = author             # Public attribute
        self._is_checked_out = False     # Private attribute

    def is_available(self):
        return not self._is_checked_out

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def __str__(self):
        status = "Available" if self.is_available() else "Checked Out"
        return f"'{self.title}' by {self.author} [{status}]"


class Library:
    def __init__(self):
        self._books = []  # Private list to hold Book instances

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
        else:
            print("Only Book instances can be added.")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"You have checked out '{book.title}'.")
                return
        print(f"Book '{title}' is either not available or doesn't exist.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"'{book.title}' has been returned.")
                return
        print(f"No record of '{title}' being checked out.")

    def list_available_books(self):
        available = [book for book in self._books if book.is_available()]
        if available:
            print("Available books:")
            for book in available:
                print(f"- {book.title} by {book.author}")
        else:
            print("No books currently available.")