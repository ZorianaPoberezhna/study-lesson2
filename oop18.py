class Book:
    _total_copies = 0

    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self._copies = copies
        Book._total_copies += copies

    @property
    def copies(self):
        return self._copies

    @copies.setter
    def copies(self, value):
        if value >= 0:
            Book._total_copies += (value - self._copies)
            self._copies = value
        else:
            raise ValueError("The number of copies cannot be negative")

    @classmethod
    def update_total_copies(cls, new_total):
        cls._total_copies = new_total

    def check_availability(self):
        return self._copies > 0

    @staticmethod
    def validate_isbn(isbn):
        return isinstance(isbn, str) and len(isbn) == 13 and isbn[:4] == 'ISBN'

    @classmethod
    def total_copies(cls):
        return cls._total_copies


class User:
    def __init__(self, name, user_id):
        self.name = name
        self._user_id = user_id
        self._borrowed_books = []

    @property
    def borrowed_books(self):
        return self._borrowed_books

    def borrow_book(self, book, library):
        if book in library.books and book.check_availability():
            self._borrowed_books.append(book)
            book.copies -= 1
            print(f"{self.name} took the book '{book.title}'")
        else:
            print(f"The book '{book.title}' was not taken.")

    def return_book(self, book, library):
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)
            book.copies += 1
            print(f"{self.name} returned the book '{book.title}'")
        else:
            print(f"The book '{book.title}' was not taken")

    @property
    def user_id(self):
        return self._user_id


class Customer(User):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)
        self._library = None

    def register_in_library(self, library):
        self._library = library
        library.register_user(self)
        print(f"{self.name} is registered in library {library.name}")


class Employee(User):
    def __init__(self, name, user_id, salary):
        super().__init__(name, user_id)
        self._salary = salary
        self._library = None

    @property
    def salary(self):
        return self._salary

    def add_book(self, book, library):
        library.add_book(book)
        print(f"{self.name}  added the book '{book.title}' to the library.")

    def remove_book(self, book, library):
        library.remove_book(book)
        print(f"{self.name} removed the book '{book.title}' from the library")


class Library:
    def __init__(self, name):
        self.name = name
        self._books = []
        self._users = []

    @property
    def books(self):
        return self._books

    @property
    def users(self):
        return self._users

    def add_book(self, book):
        if book not in self._books:
            self._books.append(book)

    def remove_book(self, book):
        if book in self._books:
            self._books.remove(book)

    def register_user(self, user):
        if user not in self._users:
            self._users.append(user)

    def find_book_by_isbn(self, isbn):
        for book in self._books:
            if book.isbn == isbn:
                return book
        return None

    def show_available_books(self):
        available_books = [book.title for book in self._books if book.check_availability()]
        print("Available books:", available_books)


library = Library ("Main library")

book1 = Book("Harry Potter", "J. К. Rowling", "ISBN 0-061-96436-0", 5)
book2 = Book("The Lord oh the Ring", "J. R. R. Tolkien", "ISBN 0-261-10236-2", 3)

customer = Customer("Kevin", 1)
employee = Employee("Mary", 2, 5000)

employee.add_book(book1, library)
employee.add_book(book2, library)

customer.register_in_library(library)

library.show_available_books()

customer.borrow_book(book1, library)
library.show_available_books()

customer.return_book(book1, library)
library.show_available_books()
