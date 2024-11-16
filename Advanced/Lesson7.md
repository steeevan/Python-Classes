### Lesson Plan: Abstract Classes and Class Hierarchy in Python

---

#### **1. Objectives**
- Understand what abstract classes are and their purpose in OOP.
- Learn how to create and use abstract classes with Python's `abc` module.
- Explore class hierarchy and the principles of inheritance in Python.
- Apply these concepts in a mini-project to reinforce learning.

---

#### **2. Definitions and Key Terms**
- **Abstract Class**: A class that cannot be instantiated and often includes abstract methods that must be implemented in its subclasses. Defined using the `abc` module in Python.
- **Abstract Method**: A method declared in an abstract class, with no implementation. Subclasses must implement these methods.
- **Class Hierarchy**: The organization of classes in a parent-child relationship, representing inheritance.

---

#### **3. Explanation and Examples**

**Abstract Class and Abstract Method**
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # Abstract method

class Dog(Animal):
    def make_sound(self):
        return "Woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

# Usage
dog = Dog()
cat = Cat()
print(dog.make_sound())  # Output: Woof
print(cat.make_sound())  # Output: Meow
```

**Class Hierarchy and Inheritance**
```python
class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def description(self):
        return f"{self.name} moves at {self.speed} km/h."

class Car(Vehicle):
    def __init__(self, name, speed, doors):
        super().__init__(name, speed)
        self.doors = doors

    def description(self):
        return f"{self.name} has {self.doors} doors and moves at {self.speed} km/h."

class Bike(Vehicle):
    def description(self):
        return f"{self.name} is a two-wheeler moving at {self.speed} km/h."

# Usage
car = Car("Sedan", 120, 4)
bike = Bike("Mountain Bike", 30)
print(car.description())  # Output: Sedan has 4 doors and moves at 120 km/h.
print(bike.description())  # Output: Mountain Bike is a two-wheeler moving at 30 km/h.
```

---

#### **4. Mini-Project: Library Management System**

**Problem Statement:**
Create a Library Management System where:
1. The abstract class `LibraryItem` defines abstract methods for `checkout` and `return_item`.
2. Subclasses `Book`, `Magazine`, and `DVD` implement the abstract methods and maintain additional properties.

**Implementation Steps:**

1. **Define the Abstract Class**
   ```python
   from abc import ABC, abstractmethod

   class LibraryItem(ABC):
       def __init__(self, title, item_id):
           self.title = title
           self.item_id = item_id
           self.is_checked_out = False

       @abstractmethod
       def checkout(self):
           pass

       @abstractmethod
       def return_item(self):
           pass
   ```

2. **Create Subclasses**
   ```python
   class Book(LibraryItem):
       def __init__(self, title, item_id, author):
           super().__init__(title, item_id)
           self.author = author

       def checkout(self):
           if not self.is_checked_out:
               self.is_checked_out = True
               return f"{self.title} by {self.author} checked out."
           return f"{self.title} is already checked out."

       def return_item(self):
           if self.is_checked_out:
               self.is_checked_out = False
               return f"{self.title} returned."
           return f"{self.title} was not checked out."

   class DVD(LibraryItem):
       def __init__(self, title, item_id, duration):
           super().__init__(title, item_id)
           self.duration = duration

       def checkout(self):
           if not self.is_checked_out:
               self.is_checked_out = True
               return f"DVD {self.title} checked out."
           return f"{self.title} is already checked out."

       def return_item(self):
           if self.is_checked_out:
               self.is_checked_out = False
               return f"DVD {self.title} returned."
           return f"{self.title} was not checked out."
   ```

3. **Test the System**
   ```python
   book = Book("Python Programming", "B001", "John Doe")
   dvd = DVD("Inception", "D001", 148)

   print(book.checkout())  # Output: Python Programming by John Doe checked out.
   print(book.return_item())  # Output: Python Programming returned.

   print(dvd.checkout())  # Output: DVD Inception checked out.
   print(dvd.return_item())  # Output: DVD Inception returned.
   ```

---

#### **5. Challenges and Activities**
- **Modify the Mini-Project**: Add another subclass like `Magazine` with unique properties.
- **Quiz**:
  - What is an abstract class, and why is it used?
  - How do subclasses inherit from an abstract class?
- **Coding Challenge**: Create a new abstract class `Shape` with subclasses like `Circle` and `Rectangle`, implementing methods to calculate the area and perimeter.

