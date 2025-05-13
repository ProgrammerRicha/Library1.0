class BookDecorator:
    def __init__(self, book):
        self.book = book

    def reserve(self):
        self.book.is_reserved = True
        print(f"The book '{self.book.title}' has been reserved.")
