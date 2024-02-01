class Person:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location


        
    def Greet(self):
        print(f"Hello {self.name}.")

Person1 = Person("Eric", 12, "Unknown")
Person2 = Person("steve",13, "Unknown")


Person1.Greet()
Person2.Greet()

#-------------------------------


class Person:
    def __init__(self, name, age, location):
        self.location = location
        self.name = name
        self.age = age
    def move(self, location2):
        self.location = location2
        print(f"{self.name} went to {self.location}")

Person3 = Person("Jasmine" , 21, "Lego Land")

Person3.move



#--------------------------------------------------

class Shape:
    def __init__(self, name, sides, angle):
        self.name = name
        self.sides = sides
        self.angle=angle


    def Name(self):
        print(f" This shape is a {self.name}")

    def Sides(self):
        print(f" This shape has {self.sides} sides")

    def Angle(self):
        print(f" This shape has a  angle measure of {self.angle} degrees")

shape1 = Shape("Square", 4, 90)

shape1.Name
shape1.Sides
shape1.Angle

#copy paste seprately

