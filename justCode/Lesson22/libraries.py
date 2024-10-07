
class Library:

    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, new_book):
        new_book.set_status(True)
        self.books.append(new_book)

    def remove_book(self, book):
        book.set_status(False)
        self.books.remove(book)

    def get_books(self):
        return self.books

    def find_genre(self,genre):
        find_genre_books = []
        for book in self.books:
            if book.genre == genre:
                find_genre_books.append(book)
        return find_genre_books



    def get_available_books(self):
        # available_books = list(filter(lambda book: book.get_status() is True, self.books))
        available_books = []
        for book in self.books:
            if book.get_status() is True:
                available_books.append(book)
        return available_books

