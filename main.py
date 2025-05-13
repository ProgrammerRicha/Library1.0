from core.singleton import SingletonMeta
from core.book import Book
from core.user_factory import UserFactory
from core.facade import LibrarySystemFacade
from core.command import AddBookCommand
from core.observer import DueDateNotifier, MemberObserver
from core.adapter import ExternalNotifier, NotifierAdapter
from core.decorator import BookDecorator
from datetime import datetime, timedelta

def show_menu():
    print("\n----- E-Library Menu -----")
    print("1. Add Book")
    print("2. View Books")
    print("3. Register User")
    print("4. Notify Users")
    print("5. Reserve Book")
    print("6. Borrow Book")
    print("7. Return Book")
    print("0. Exit")
    return input("Select an option: ")

def main():
    system = LibrarySystemFacade()
    factory = UserFactory()
    notifier = DueDateNotifier()
    observers = {}
    users_by_name = {}

    while True:
        choice = show_menu()

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter ISBN: ")
            category = input("Enter category: ")
            book = Book(title, author, isbn, category)
            cmd = AddBookCommand(book, system)
            cmd.execute()
            print("Book added.")

        elif choice == "2":
            print("\nAvailable Books:")
            for book in system.view_books():
                status = "Borrowed" if book.borrowed_by else "Available"
                print(f"{book} | Status: {status}")

        elif choice == "3":
            role = input("Enter user role (Member/Librarian): ")
            name = input("Enter user name: ")
            user = factory.create_user(role, name)
            system.register_user(user)
            users_by_name[name] = user
            print(f"{role} '{name}' registered.")
            if role == "Member":
                observer = MemberObserver(user)
                notifier.subscribe(observer)
                observers[name] = observer

        elif choice == "4":
            message = input("Enter message to notify members: ")
            notifier.notify(message)

        elif choice == "5":
            title = input("Enter title of book to reserve: ")
            found = False
            for book in system.view_books():
                if book.title.lower() == title.lower():
                    decorated = BookDecorator(book)
                    decorated.reserve()
                    found = True
                    break
            if not found:
                print("Book not found.")

        elif choice == "6":
            member_name = input("Enter member name: ")
            title = input("Enter title of book to borrow: ")
            member = users_by_name.get(member_name)
            if not member:
                print("Member not found.")
                continue

            for book in system.view_books():
                if book.title.lower() == title.lower():
                    if book.borrowed_by:
                        print("Book is already borrowed.")
                    else:
                        book.borrowed_by = member
                        book.due_date = datetime.now() + timedelta(days=14)
                        print(f"{member.name} borrowed '{book.title}' (Due: {book.due_date.date()})")
                    break
            else:
                print("Book not found.")

        elif choice == "7":
            member_name = input("Enter member name: ")
            title = input("Enter title of book to return: ")
            member = users_by_name.get(member_name)
            if not member:
                print("Member not found.")
                continue

            for book in system.view_books():
                if book.title.lower() == title.lower() and book.borrowed_by == member:
                    book.borrowed_by = None
                    book.due_date = None
                    print(f"{member.name} returned '{book.title}'.")
                    break
            else:
                print("No matching borrowed book found.")

        elif choice == "0":
            print("Exiting E-Library. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
