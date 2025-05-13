class Command:
    def execute(self):
        pass

class AddBookCommand(Command):
    def __init__(self, book, system):
        self.book = book
        self.system = system

    def execute(self):
        self.system.add_book(self.book)
