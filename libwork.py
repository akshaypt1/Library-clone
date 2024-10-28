class Book:
    def __init__(self, name, author, number):
        self.name = name
        self.author = author
        self.number = number

    def __str__(self):
        return f"Name: {self.name}, Author: {self.author}, Number: {self.number}"


class User:
    def __init__(self, username):
        self.username = username
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book.name)

    def return_book(self, book_name):
        if book_name in self.borrowed_books:
            self.borrowed_books.remove(book_name)
            return True
        return False


class Library:
    def __init__(self):
        self.books = []
        self.users = {}
        self.admin_username = "akshay"
        self.admin_password = "akshay123"

    def admin_login(self):
        username = input("Enter admin name: ")
        password = input("Enter password: ")
        if username == self.admin_username and password == self.admin_password:
            self.admin_menu()
        else:
            print("Invalid admin name or password")

    def user_login(self):
        username = input("Enter username: ")
        if username not in self.users:
            print("User not found. Please register first.")
            return
        password = input("Enter password: ")
        if self.users[username] == password:
            self.user_menu(User(username))
        else:
            print("Invalid user name or password")

    def admin_menu(self):
        while True:
            print("\nAdmin Menu:")
            print("1. Add Book")
            print("2. Delete Book")
            print("3. Show All Books")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.delete_book()
            elif choice == "3":
                self.show_books()
            elif choice == "4":
                print("Exited Admin Menu.")
                break
            else:
                print("Invalid option.")

    def user_menu(self, user):
        while True:
            print("\nUser Menu:")
            print("1. Show Books Taken by User")
            print("2. Return Book")
            print("3. Borrow Book")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.show_user_books(user)
            elif choice == "2":
                self.return_book(user)
            elif choice == "3":
                self.borrow_book(user)
            elif choice == "4":
                print("Exited User Menu.")
                break
            else:
                print("Invalid option.")

    def add_book(self):
        book_name = input("Enter book name: ")
        author_name = input("Enter author name: ")
        book_number = input("Enter book number: ")
        new_book = Book(book_name, author_name, book_number)
        self.books.append(new_book)
        print(f"Book '{book_name}' by '{author_name}' added.")

    def delete_book(self):
        book_name = input("Enter the name of the book to delete: ")
        for book in self.books:
            if book.name.lower() == book_name.lower():
                self.books.remove(book)
                print(f"Book '{book_name}' has been deleted.")
                return
        print(f"Book '{book_name}' not found.")

    def show_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Available books:")
            for book in self.books:
                print(f"- {book}")

    def show_user_books(self, user):
        if user.borrowed_books:
            print(f"{user.username} has borrowed the following books:")
            for book in user.borrowed_books:
                print(f"- {book}")
        else:
            print(f"{user.username} has not borrowed any books.")

    def return_book(self, user):
        book_name = input("Enter the name of the book to return: ")
        if user.return_book(book_name):
            print(f"Book '{book_name}' has been returned.")
        else:
            print(f"{user.username} has not borrowed the book '{book_name}'.")

    def borrow_book(self, user):
        self.show_books()
        book_name = input("Enter the name of the book to borrow: ")
        for book in self.books:
            if book.name.lower() == book_name.lower():
                user.borrow_book(book)
                self.books.remove(book)
                print(f"Book '{book_name}' has been borrowed.")
                return
        print(f"Book '{book_name}' not found.")

    def register_user(self):
        username = input("Enter a new username: ")
        if username in self.users:
            print("Username already exists.")
            return
        password = input("Enter a password: ")
        self.users[username] = password
        print(f"User '{username}' registered successfully.")

    def start(self):
        while True:
            print("Welcome to the Library")
            print("1. Login as Admin")
            print("2. Login as User")
            print("3. Register User")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.admin_login()
            elif choice == "2":
                self.user_login()
            elif choice == "3":
                self.register_user()
            elif choice == "4":
                print("Exited Library System.")
                break
            else:
                print("Invalid option.")

library = Library()
library.start()
