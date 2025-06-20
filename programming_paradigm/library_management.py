class Book:
    def __init__(self, title, author):
        """
        Initialize a Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """
        Mark the book as checked out.
        """
        self._is_checked_out = True

    def return_book(self):
        """
        Mark the book as returned.
        """
        self._is_checked_out = False

    def is_available(self):
        """
        Check if the book is available.

        Returns:
            bool: True if the book is available, False otherwise.
        """
        return not self._is_checked_out

    def __str__(self):
        """
        Return a string representation of the Book object.

        Returns:
            str: A string in the format "title by author".
        """
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        """
        Initialize a Library object.
        """
        self._books = []

    def add_book(self, book):
        """
        Add a book to the library.

        Args:
            book (Book): The book to add.
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Check out a book from the library.

        Args:
            title (str): The title of the book to check out.
        """
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.is_available():
                    book.check_out()
                    print(f"Checked out '{title}'")
                else:
                    print(f"'{title}' is not available for checkout.")
                return
        print(f"'{title}' not found in the library.")

    def return_book(self, title):
        """
        Return a book to the library.

        Args:
            title (str): The title of the book to return.
        """
        for book in self._books:
            if book.title.lower() == title.lower():
                if not book.is_available():
                    book.return_book()
                    print(f"Returned '{title}'")
                else:
                    print(f"'{title}' is already available in the library.")
                return
        print(f"'{title}' not found in the library.")

    def list_available_books(self):
        """
        List all available books in the library.
        """
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(book)
