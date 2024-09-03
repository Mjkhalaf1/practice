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
            self.books[book] = int(self.books[book])
            if self.books[book] > 0:
                self.books[book] -= 1
            if self.books[book] == 0 and self.borrowedBooks[book.name] == 0:
                del self.books[book]
        else:
            print("The book does not exist!")
        
    def lendBook(self, patron , book):
        if book in self.books.keys():
            self.books[book] = int(self.books[book])
            if(self.books[book] > 0):
                print("A book is lent.")
                self.books[book] -= 1 
                if book.name in self.borrowedBooks.keys():
                    self.borrowedBooks[book.name] += 1
                else:
                    self.borrowedBooks[book.name] = 1
                patron.borrowedBooks.append(book.name)
            else:
                print("All books are lent!")
        else:
            print("The book does not exist!")
    def returnBook(self, patron , book):
        if book.name in self.borrowedBooks.keys():
            self.borrowedBooks[book.name] -= 1
            if self.borrowedBooks[book.name] == 0:
                del self.borrowedBooks[book.name]
            if(book not in self.books.keys()):
                self.addBook(book,1)
            else:
                self.books[book] += 1    
            print("You have successfuly returned the book.")
            patron.borrowedBooks.remove(book.name)
        else:
            print("This book is not borrowed!")
        
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
        if book in self.books:
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
print("-------------------------------")
print("Welcome to my library system.")
print("-------------------------------")
print("""Enter 1 to create a library instance
Enter 2 to create a book instance
Enter 3 to create a patron instance
Enter 4 to add a book to the library
Enter 5 to remove a book from the library
Enter 6 to borrow a book
Enter 7 to return a book
Enter 8 to show all books in the library
Enter 9 to show all borrowed books in the library
Enter 10 to transfer a book to another library
Enter 11 to show all books in two libraries
Enter 12 to show borrowed books for a patron""")
libraries = {}
books = {}
patrons = {}
i = 0
while i != -1:
    i = int(input("Enter the number for your process:"))
    match i:
        case 1:
            libraryName = input("Enter the library name:")
            libraryLocation = input("Enter the library location:")
            libraryIns = Library(libraryName , libraryLocation)
            libraries[libraryName] = libraryIns
            print("A library instance is created successfuly")
        case 2:
             bookName = input("Enter the book name:")
             bookAuthor = input("Enter the book author:")
             bookType = input("Enter the book type:")
             bookIns = Book(bookName , bookAuthor , bookType)
             books[bookName] = bookIns
             print("A book instance is created successfuly")
        case 3:
            patronName = input("Enter the patron Name:")
            patronIns= Patron(patronName)
            patrons[patronName] = patronIns
            print("A patron instance is created successfuly")
        case 4:
            libraryName = input("Enter the library name:")
            bookName = input("Enter the book name:")
            numbers = input ("Enter the numbers of this book:")
            libraries[libraryName].addBook(books[bookName],numbers)
            print("The book is added")
        case 5:
            libraryName = input("Enter the library name:")
            bookName = input("Enter the book name:")
            libraries[libraryName].removeBook(books[bookName])
            print("The book is removed")
        case 6: 
            libraryName = input("Enter the library name:")
            bookName = input("Enter the book name:")
            patronName = input("Enter the patron Name:")
            libraries[libraryName].lendBook(patrons[patronName],patrons[patronName])
            print(f"{patronName} has borrowed {bookName}")
            
            