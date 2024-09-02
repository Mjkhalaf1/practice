class Library:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.books = {}
        self.borrowedBooks = {}
    def addBook(self, book , numbers):
        print("A book is added to the library.")
        if book not in self.books.keys():
            self.books[book] = numbers
        else:
            self.books[book] += numbers 
    def removeBook(self, book):
        if book in self.books.keys():
            print("A book is removed from the library.")
            if self.books[book] > 0:
                self.books[book] -= 1
            if self.books[book] == 0 and self.borrowedBooks[book.name] == 0:
                del self.books[book]
        else:
            print("The book does not exist!")
        
    def lendBook(self, patron , book):
        if(self.books[book] > 0):
            print("A book is lent.")
            self.books[book] -= 1 
            if book.name in self.borrowedBooks.keys():
                self.borrowedBooks[book.name] += 1
            else:
                self.borrowedBooks[book.name] = 1
            patron.borrowedBooks.append(book.name)
        else:
            print("All books are lent! OR it does not exist!")
    def returnBook(self, patron , book):
        self.borrowedBooks[book.name] -= 1
        if self.borrowedBooks[book.name] == 0:
            del self.borrowedBooks[book.name]
        if(book not in self.books.keys()):
            self.addBook(book,1)
        else:
            self.books[book] += 1    
        print("You have successfuly returned the book.")
        patron.borrowedBooks.remove(book.name)
        
    def showBooks(self):
        print(f"All the books in this library:{self.name}")
        for book in self.books.keys():
            print(f"{book.name} -- {book.author} -- {book.type} -- (borrowed:{self.borrowedBooks.get(book.name,0)})"
                f" There are {self.books[book]} to borrow.")
    def listBorrowed(self):
        print("The borrowed books are:")
        for i,j in self.borrowedBooks.items():
            print(i , "---", j)
    def transferBook(self , other , book, num):
        numTransfered = min(num , self.books[book])
        print(f"{numTransfered} are trnasfered to {other.name}")
        for i in range(num):
            self.removeBook(book)
        other.addBook(book,numTransfered)
    def __add__(self, other):
        self.showBooks()
        other.showBooks()
        return "Addition performed between library1 and library2"
        
class Book:
    def __init__(self, name, author, type):
        self.name = name
        self.author = author
        self.type = type

class Ebook(Book):
    def __init__(self, name, author, type, format):
        super().__init__(name , author, type)
        self.format = format
        
class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowedBooks = []
    def pateronBooks(self):
        print(f"{self.name} has borrowed {len(self.borrowedBooks)}")
        for book in self.borrowedBooks:
            print(book)
            
#-----------------------------------------------------------------------------------------#
            
library1 = Library("UOB Lib" , "Manama")
book1 = Book("Calaculus" , "Fahad" , "Math")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")
book3 = Book("1984", "George Orwell", "Dystopian" )
book4 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic")
book5 = Book("Introduction to Algorithms", "Thomas H. Cormen", "Computer Science")
book6 = Book("A Brief History of Bahrain", "Hasan alEbrahimi", "History")
book7= Ebook("Cloud Computing", "Khalaf", "IT" , "PDF")
library1.addBook(book1,4)
library1.addBook(book2,2)
library1.addBook(book3,2)
library1.addBook(book4,2)
library1.addBook(book5,2)
library1.addBook(book6,2)
library1.addBook(book7,1)
library1.removeBook(book3)
library2 = Library("PolyLib", "Raffa")
library1.transferBook(library2,book1,2)
library2.addBook(book6,10)
print(library1 + library2)





           