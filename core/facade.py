from .singleton import SingletonMeta

class LibrarySystemFacade(metaclass=SingletonMeta):
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def register_user(self, user):
        self.users.append(user)

    def view_books(self):
        return self.books
