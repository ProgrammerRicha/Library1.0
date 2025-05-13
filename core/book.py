class Book:
    def __init__(self, title, author, isbn, category):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.category = category
        self.is_reserved = False
        self.borrowed_by = None
        self.due_date = None

    def __str__(self):
        return f"{self.title} by {self.author} | ISBN: {self.isbn} | Category: {self.category}"
