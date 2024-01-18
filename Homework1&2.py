#LESSON 1

#Problem 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}!")

person1 = Person("Justin", 11)
person2 = Person("Estevan", 23)

person1.greet()
person2.greet()

#Problem 2
class Person:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def greet(self):
        print(f"Hello, my name is {self.name}!")

    def move(self, new_location):
        self.location = new_location
        print(f"{self.name} has located to {self.location}")

person3 = Person( "Justin", 11, "Chino Hills")
        
        

person1 = Person("Justin", 11)
person2 = Person("Estevan", 23)

person1.greet()
person2.greet()

#Problem 3
class Animal:
    def __init__(self, species, texture, location):
        self.species = species
        self.texture = texture
        self.location = location
        
    def name(species):
        print(f"This animal is a {self.species}")

    def feel(texture):
        print(f"This animal has {self.texture} skin")
        
    def place(self, location):
        print(f"This animal is located in {self.location}")
animal1 = Person("Panda", "furry" ,  "China")

#LESSON 2

#Problem 1
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}!")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Bark")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")

dog_namne = Dog("Lucky")
cat_name = Cat("Celine")


dog_name.make_sound()
cat_name.make_sound()

#Problem 2
def perform_action(animal):
    animal.make_sound()
    animal.move()
    
perform_action(dog_name)
perform_action(cat_name)

#Problem 3
class Person:
    def __init__(self, name, age):
        self.name = names
        self.age = age
    def greeting(name):
        print(f"Hi my name is {self.name} and I am {self.age} years old!")
class Years(age):
    def __init__(self, name):
        super().__init__(name, 14)
person_name = Person("Austin")

person_age = Person("14")
