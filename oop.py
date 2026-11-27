class Book:
    def __init__(self, book_id, title, author, is_available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = is_available


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        for existing_book in self.books:
            if existing_book.book_id == book.book_id:
                print("Error: Book ID already exists!")
                return
        self.books.append(book)
        print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("No books available in the library.")
            return

        print("========== BOOK LIST ==========")
        for book in self.books:
            status = "Available" if book.is_available else "Issued"
            print(f"Book ID: {book.book_id}")
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"Status: {status}")
            print("-" * 31)

    def search_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                status = "Available" if book.is_available else "Issued"
                print("Book Found!")
                print(f"Book ID: {book.book_id}")
                print(f"Title: {book.title}")
                print(f"Author: {book.author}")
                print(f"Status: {status}")
                return book
        print("Error: Book not found!")
        return None

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_available:
                    book.is_available = False
                    print("Book issued successfully!")
                else:
                    print("Sorry! This book is already issued.")
                return
        print("Error: Book not found!")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_available:
                    book.is_available = True
                    print("Book returned successfully!")
                else:
                    print("This book was not issued.")
                return
        print("Error: Book not found!")


def main():
    library = Library()

    while True:
        print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            try:
                book_id = int(input("Enter Book ID: "))
                title = input("Enter Book Title: ")
                author = input("Enter Author Name: ")
                new_book = Book(book_id, title, author)
                library.add_book(new_book)
            except ValueError:
                print("Error: Book ID must be a number!")

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            try:
                book_id = int(input("Enter Book ID: "))
                library.search_book(book_id)
            except ValueError:
                print("Error: Book ID must be a number!")

        elif choice == "4":
            try:
                book_id = int(input("Enter Book ID: "))
                library.issue_book(book_id)
            except ValueError:
                print("Error: Book ID must be a number!")

        elif choice == "5":
            try:
                book_id = int(input("Enter Book ID: "))
                library.return_book(book_id)
            except ValueError:
                print("Error: Book ID must be a number!")

        elif choice == "6":
            print("Exiting Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice! Please select an option from 1 to 6.")

if __name__ == "__main__":
    main()