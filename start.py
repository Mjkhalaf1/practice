class Library:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.books = []
        self.borrowedBooks = {}
    def addBook(self, book):
        print("A book is added to the library.")
        self.books.append(book)
    def removeBook(self, book):
        print("A book is removed from the library.")
        self.books.remove(book)
    def lendBook(self, patron , book):
        if(book.borrowed == False):
            print("A book is lent.")
            book.borrowed = True
            self.borrowedBooks[patron.name] = book.name
            patron.borrowedBooks.append(book.name)
        else:
            print("This book is already borrowed!")
    def showBooks(self):
        print("All the books in the library:")
        for book in self.books:
            print(f"{book.name} -- {book.author} -- {book.type} -- ({book.borrowed})")
    def listBorrowed(self):
        print("The borrowed books are:")
        for i,j in self.borrowedBooks.items():
            print(i , "---", j)
        

class Book:
    def __init__(self, name, author, type):
        self.name = name
        self.author = author
        self.type = type
        self.borrowed = False

class Ebook(Book):
    def __init__(self, name, author, type, format, hyperlink):
        super.__init__(name , author, type)
        self.format = format
        self.hyperlink = hyperlink
class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowedBooks = []
    def pateronBooks(self):
        print(f"{self.name} has borrowed {len(self.borrowedBooks)}")
        for book in self.borrowedBooks:
            print(book)
            
library1 = Library("UOB Lib" , "Manama")
book1 = Book("Calaculus" , "Fahad" , "Math")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")
book3 = Book("1984", "George Orwell", "Dystopian")
book4 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic")
book5 = Book("Introduction to Algorithms", "Thomas H. Cormen", "Computer Science")
book6 = Book("A Brief History of Baharin", "Hasan alEbrahimi", "History")
library1.addBook(book1)
library1.addBook(book2)
library1.addBook(book3)
library1.addBook(book4)
library1.addBook(book5)
library1.addBook(book6)
library1.removeBook(book3)
p1 = Patron("Mohamed")
library1.lendBook(p1, book6)
library1.listBorrowed()
library1.showBooks()
p2 = Patron("Hasan")
library1.lendBook(p2,book6)
library1.lendBook(p1,book1)
p1.pateronBooks()



           