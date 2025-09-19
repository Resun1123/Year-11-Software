class Book: #create the Book class
    def __init__(self, book_id, title, author): #giving it properties
        self.book_id = book_id 
        self.title = title 
        self.author = author 
        self.is_loaned = False #Boolean variable

class Borrower:
    def __init__(self, borrower_id, name): # create a borrower class
        self.borrower_id = borrower_id 
        self.name = name

class Loan:
    def __init__(self, book, borrower):
        self.book = book
        self.borrower = borrower # create a loan class that takes a book and borrower as parameters 
#This class will manage the loaning of books to borrowers. It will keep track of which book is being loaned and to whom.

class BookManager:
    def __init__(self):
        self.books = {}# This will hold the books in a dictionary with book_id as the key
# This will allow us to easily add, remove, and search for books by their ID because its a dictionary
    def add_book(self, book_id, title, author):
        if book_id in self.books:
            raise ValueError("Book ID already exists.") # Check if the book already exists in the dictionary so there is no duplicates
        self.books[book_id] = Book(book_id, title, author) # if it does not exist, this will create a new Book object and add to the dictionary. 

    def remove_book(self, book_id): # This function remove a book from the dictionary using a book Id number
        # If the book_id exists in the dictionary, it will delete it, otherwise it will raise a ValueError 
        if book_id in self.books:
            del self.books[book_id]
        else:
            raise ValueError("Book ID not found.")

    def search_book(self, book_id): # Using this function, we can search for a book by its id
        return self.books.get(book_id, None)

class BorrowerManager: # This Class will manage the borrowers of the library and put them in a dictionary with borrower_id as the key
    def __init__(self):
        self.borrowers = {}

    def add_borrower(self, borrower_id, name): # If borrower_id already exists, it will raise a ValueError
        # If it does not exist, it will create a new Borrower object and add it to the dictionary
        if borrower_id in self.borrowers:
            raise ValueError("Borrower ID already exists.")
        self.borrowers[borrower_id] = Borrower(borrower_id, name)

    def remove_borrower(self, borrower_id): #This function will remove a borrower from the dictionary using a borrower_id
        # If the borrower_id exists in the dictionary, it will delete it, otherwise it will raise a ValueError
        if borrower_id in self.borrowers:
            del self.borrowers[borrower_id]
        else:
            raise ValueError("Borrower ID not found.")

    def search_borrower(self, borrower_id):
        return self.borrowers.get(borrower_id, None)

class LoanManager: # This class manages the loans of books to the borrowers
# It will keep track of all the loans made in the library
    def __init__(self):
        self.loans = []

    def create_loan(self, book, borrower): # This function will create a loan for a book to a borrower
        if book.is_loaned:
            raise ValueError("Book is already loaned.")
        loan = Loan(book, borrower)
        self.loans.append(loan)
        book.is_loaned = True

    def return_loan(self, book):
        for loan in self.loans:
            if loan.book.book_id == book.book_id:
                self.loans.remove(loan)
                book.is_loaned = False
                break

class LibraryFacade: # This class provides a simplified interface to the complex system that manages books, loan, and borrowers in the backend
# It will use the BookManager, BorrowerManager, and LoanManager classes to perform operations on the library
    def __init__(self):
        self.book_manager = BookManager()
        self.borrower_manager = BorrowerManager()
        self.loan_manager = LoanManager()

    def add_book(self, book_id, title, author):
        self.book_manager.add_book(book_id, title, author)

    def remove_book(self, book_id):
        self.book_manager.remove_book(book_id)

    def search_book(self, book_id):
        return self.book_manager.search_book(book_id)

    def add_borrower(self, borrower_id, name):
        self.borrower_manager.add_borrower(borrower_id, name)

    def remove_borrower(self, borrower_id):
        self.borrower_manager.remove_borrower(borrower_id)

    def search_borrower(self, borrower_id):
        return self.borrower_manager.search_borrower(borrower_id)

    def create_loan(self, book_id, borrower_id):
        book = self.book_manager.search_book(book_id)
        borrower = self.borrower_manager.search_borrower(borrower_id)
        if book and borrower:
            self.loan_manager.create_loan(book, borrower)
        else:
            raise ValueError("Book or Borrower not found.")

    def return_loan(self, book_id):
        book = self.book_manager.search_book(book_id)
        if book:
            self.loan_manager.return_loan(book)
        else:
            raise ValueError("Book not found.")
if __name__ == "__main__":
    library = LibraryFacade()

    # Adding books
    library.add_book(1, "The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book(2, "1984", "George Orwell")

    # Adding borrowers
    library.add_borrower(1, "Alice")
    library.add_borrower(2, "Bob")

    # Creating a loan
    library.create_loan(1, 1)  # Alice borrows "The Great Gatsby"

    # Searching for a book
    book = library.search_book(1)
    print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Is Loaned: {book.is_loaned}")

    # Returning a loan
    library.return_loan(1)

    # Checking the book status again
    book = library.search_book(1)
    print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Is Loaned: {book.is_loaned}")
