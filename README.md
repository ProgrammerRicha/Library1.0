# E-Library System

## 📚 Description
This is a console-based E-Library system implemented in Python using key software design patterns. The system supports book management, user registration, loan processing, and notification—all using in-memory data.

---

## 🚀 How to Run

1. **Download or Clone the Repository**
2. Make sure you have **Python 3.x** installed.
3. Open terminal in the project directory.
4. Run the app:
```bash
python main.py
```

---

## 📋 Features

- Add, View, Reserve, Borrow, and Return Books
- Register Members and Librarians
- Notify members via console output
- Due date tracking for borrowed books

---

## 🧠 Design Patterns Used

| Pattern Type  | Design Pattern   | Purpose |
|---------------|------------------|---------|
| Creational    | Singleton         | Ensures single instances of catalogue/system |
|               | Factory Method    | Creates different user types |
| Structural    | Adapter           | Integrates external notification system |
|               | Decorator         | Adds reserve functionality to books |
|               | Facade            | Simplifies interface for library actions |
| Behavioral    | Command           | Encapsulates book operations |
|               | Observer          | Notifies users of due dates |
|               | Iterator (Implicit)| Iterates over books/users list |

---

## 🧪 Sample Commands
```
1. Add Book
2. View Books
3. Register User
4. Notify Users
5. Reserve Book
6. Borrow Book
7. Return Book
0. Exit
```

