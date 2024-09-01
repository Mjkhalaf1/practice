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
        if book in self.books:
            print("A book is removed from the library.")
            book.numbers -= 1
            if book.numbers == 0:
                self.books.remove(book)
        else:
            print("The book does not exist!")
        
    def lendBook(self, patron , book):
        if(book.numbers > 0):
            print("A book is lent.")
            book.numbers -= 1
            book.borrowed += 1 
            if patron.name in self.borrowedBooks:
                self.borrowedBooks[patron.name].append(book.name)
            else:
                self.borrowedBooks[patron.name] = [book.name]
            patron.borrowedBooks.append(book.name)
        else:
            print("All books are lent! OR it does not exist!")
    def returnBook(self, patron , book):
        book.borrowed -= 1
        if(book not in self.books):
            self.addBook(book)
            book.numbers = 1
        else:
            book.numbers =+ 1    
        print("You have successfuly returned the book.")
        patron.borrowedBooks.remove(book.name)
        if len(self.borrowedBooks[patron.name]) > 1:
            self.borrowedBooks[patron.name].remove(book.name)
        else:
            self.borrowedBooks.pop(patron.name)
        
    def showBooks(self):
        print("All the books in the library:")
        for book in self.books:
            print(f"{book.name} -- {book.author} -- {book.type} -- ({book.borrowed}:borrowed)"
                f" There are {book.numbers} to borrow.")
    def listBorrowed(self):
        print("The borrowed books are:")
        for i,j in self.borrowedBooks.items():
            print(i , "---", j)
    def transferBook(self , other , book, num):
        numTransfered = min(num , book.numbers)
        print(f"{numTransfered} are trnasfered")
        for i in range(num):
            self.removeBook(book)
        other.addBook(book)
        

         
        
class Book:
    def __init__(self, name, author, type, number):
        self.name = name
        self.author = author
        self.type = type
        self.numbers = number
        self.borrowed = 0

class Ebook(Book):
    def __init__(self, name, author, type, format):
        super.__init__(name , author, type)
        self.format = format
        self.accessed = 0
        
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
book1 = Book("Calaculus" , "Fahad" , "Math" , 4)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction" , 2)
book3 = Book("1984", "George Orwell", "Dystopian" , 2)
book4 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic", 2)
book5 = Book("Introduction to Algorithms", "Thomas H. Cormen", "Computer Science", 2)
book6 = Book("A Brief History of Bahrain", "Hasan alEbrahimi", "History" ,2)
library1.addBook(book1)
library1.addBook(book2)
library1.addBook(book3)
library1.addBook(book4)
library1.addBook(book5)
library1.addBook(book6)
library1.removeBook(book3)
p1 = Patron("Mohamed")
p2 = Patron("Hasan")
library2 = Library("PolyLib" , "Raffa")
library1.lendBook(p1,book6)
library1.transferBook(library2, book6 , 2)
library2.showBooks()
library1.returnBook(p1,book6)
library1.showBooks()


           