from .user import Member, Librarian

class UserFactory:
    def create_user(self, user_type, name):
        if user_type == "Member":
            return Member(name)
        elif user_type == "Librarian":
            return Librarian(name)
        else:
            raise ValueError("Invalid user type")
