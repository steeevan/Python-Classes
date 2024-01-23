import time

'''
homework OOP
'''
#i pretty much just based it off the class code and added a location attribute, i couldn't exactly figure out how i should implement the speech part of the location so i just slapped it on the end of 'greet'
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello. My name {self.name} and I am {self.age} years old. I am currently in {self.place}")
    def location(self, place):
        self.place = place
        
person1 = person("Alton",13)
person2 = person("Nobody", 0)

person1.location("Chino Hills")
person1.greet()
time.sleep(3.5)
print("")
print("")
person1.location("Paris")
person1.greet()

#i think a reasonable application would be similar to a gun, like put reload and fire attributes

class gun:
    def __init__(self, name)
        self.name = name
    def fire(self)
        bullets = 30
        shoot = bullets - 1

#however i could not get this to work because it was a bit too complex :(
'''
homework Polymorphism and Inheritance
'''
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def make_sound(self):
        print(f"{self.name}: {self.sound}.")
    def move(self):
        print(f"{self.name} dipped!")
    def action(self):
        self.make_sound()
        self.move()

class raccoon(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)

class snake(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)

Snake = snake("Jotaro Kujo", "hisssss")
Raccoon = raccoon("Joe", "idk")

Raccoon.make_sound()
Snake.make_sound()

def perform_action(tAnimal):
    tAnimal.action()

perform_action(Raccoon)
perform_action(Snake)

#i think a real world application of inheritance is probably something like a disease

class Disease:
    def __init__(self, name, symptoms):
        self.name = name
        self.symptoms = symptoms
    def display_info(self):
        print(f"{self.name} has these symptoms: {self.symptoms}")
    def victim(self, person):
        self.person = person
    def infect(self):
        print(f"{self.name} has infected a person!")

class COVID_19(Disease):
    def __init__(self, name, symptoms):
        super().__init__(name, symptoms)

class Black_Death(Disease):
    def __init__(self, name, symptoms):
        super().__init__(name, symptoms)

Covid = COVID_19("COVID-19", "Fluid Discharge, Fever, Fatigue, Headaches, Nausea or Vomiting, Loss of Taste and Smell")
BDeath = Black_Death("Black Death", "Fluid Discharge, Fever, Fatigue, Headaches, Nausea or Vomiting, Skin Discoloration")

Covid.display_info()
BDeatg.display_info()

def infec_t(tDisease):
    tDisease.infect()

infec_t(Covid)
infec_t(BDeath)
