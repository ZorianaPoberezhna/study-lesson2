class Book:
    def __init__(self, title, author):
        self.tittle = title
        self.author = author


    def __eq__(self, other):
        if isinstance(other, Book):
            return self.tittle == other.tittle and self.author == other.author
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

book1 = Book("Title1", "Author1")
book2 = Book("Title2", "Author2")
print(book1 == book2)
print(book1 != book2)