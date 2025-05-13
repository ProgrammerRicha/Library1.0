class User:
    def __init__(self, name):
        self.name = name

class Member(User):
    def __init__(self, name):
        super().__init__(name)
        self.role = "Member"

class Librarian(User):
    def __init__(self, name):
        super().__init__(name)
        self.role = "Librarian"
