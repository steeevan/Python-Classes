#Inheritance and Polymorphism

'''
Inheritance: A mechanism where a new class(subclass
inherits properties and behavior from an existing
class(superclass)

Polymorphism: The ability of different classes to be treated as
instances of the same class through a common interface
'''

#Problem 1
'''
Create a subclass Ebook that inherits from the Book class. Add
a new attribute' file_size' and a method 'read_book' to
the Ebook class

'''

'''
Class Name: Book
Description: This defines a class which contains title, author and pages of a book.
This has one method which displays the books inforamtion.
'''
class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"Title: {self.title} , Author: {self.author},Pages: {self.pages}")

    def update_title(self, new_title):
        self.title = new_title
    def update_author(self, new_author):
        self.author = new_author
    def update_pages(self, new_pages):
        self.pages = new_pages


'''
Class Name: EBook
Description: THis is going to inherit the Book class, and add new attributes.
'''
class EBook(Book):
    def __init__(self,title,author,pages,fs):
        super().__init__(title,author,pages)
        self.file_size = fs

    def read_book(self):
        print(f"Reading the eBook '{self.title}' with file size {self.file_size} MB.")
    

book1 = EBook("Hunger Games Pt.1", "Suzanne Collins", 384,15)
print(book1)

book1.display_info()
book1.read_book()
book1.update_pages(500)
book1.display_info()


book2 = Book("Captain Underpants","Justin",35)
book2.display_info()
book2.update_pages(1000000000)
book2.display_info()

#Polymorphism
def print_info(tbook):
    tbook.display_info()
print("-------------------------------")
print_info(book1)
print_info(book2)

