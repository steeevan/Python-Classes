'''
Person is a class that has the attributes of their name, age, and location.
It has the greet method and move method.
'''
class Person:
    def __init__(self,name,age,location):
        self.name = name
        self.age = age
        self.location = location
    def greet(self):
        print(f"Hello my name is {self.name} and nice to meet you! I am {self.age} years old.")
    def move(self,tLocation):
        print(f"Originally at: {self.location}")
        self.location = tLocation
        print(f"Now at: {self.location}")
person = Person("Tyler",24,"")

person2 = Person("Dan",19,"")

person3 = Person("Poe",41,"")

person4 = Person("Mouse",30,"Caesars Palace")

person.greet()
person2.greet()
person3.greet()
person4.greet()
person4.move("Las Vegas")

print("---------------------------------------------------------------------------------------------------------")

'''
You are making the blueprint of a table. The height, width, and material will be
my attributes.
'''
class Table:
    def __init__(self,height,width,material):
        self.height = height
        self.width = width
        self.material = material
    def change_height(self,tHeight):
        print(f"Height is originally: {self.height}")
        self.height = tHeight
        print(f"Height is now: {self.height}")
    def change_width(self,tWidth):
        print(f"Width is originally: {self.width}")
        self.width = tWidth
        print(f"Width is now: {self.width}")
    def change_material(self,tMaterial):
        print(f"Material is originally: {self.material}")
        self.material = tMaterial
        print(f"Material is now: {self.material}")
table = Table(50,50,"Wood")

table.change_height(100)

table.change_width(100)

table.change_material("Plywood")















