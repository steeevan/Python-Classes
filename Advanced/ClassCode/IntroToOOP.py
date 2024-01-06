#Introduction to Object Oriented Programming (OOP) in Python
'''
1. Object Oriented Programming:
    OOP is a programming paradigm that organize code into obkects.
    Objects have both data(attributes) and behavior(methods)
    associated to them.

2. Class:
    A class is a blueprint for creating objects. It defines
    the structure and behavior that its
    instances(objects) will have.

3. Object:
    An instance of a class, representing a specitic entity
    in the program.

    
'''

# Exercises 1
# Define a class called Book, with attributes 'title',
# 'author', and 'page'. Include methods such as
# 'display_info', that prints the books information

class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"Title: {self.title} , Author: {self.author},Pages: {self.pages}")
        

#First book
book1 = Book("Python Advanced","Estevan",1)
book2 = Book("Python Basic", "Estevan", 2)
book3 = Book("Python Int.","Estevan",3)
book4 = Book("Python baby edition", "Estevan", 5)
book5 = Book("Python Elders","Estevan",0)


# Show info of my books
book1.display_info()
book2.display_info()
book3.display_info()
book4.display_info()
book5.display_info()


library = [book1,book2,book3,book4,book5]

for i in library:
    i.display_info()

# Challenge 1
# Create 4 new books
# Create a list named Lirary and append all 5 books to this list.
# Optional: Create a for loop that displays info of each book

'''
How does the concept of a class relate to real-world entities?
 - Objects that you interact with For example, 'Book' class might represent
  a real book.
  
What is the purpose of the __init__ method in a class?
 - This is a special method in Python that helps us initialize an object.
 
Explain the difference between a class and an object?
    - A class is a template or blueprint. Ab object is an instance of a class
'''
