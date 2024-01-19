'''
We are creating a superclass, that has the properties "Name, Sound".
The methods are make_sound, move, and perform_action.
'''
class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
    def make_sound(self):
        print(f"This animal makes the sound {self.sound}.")
    def move(self):
        print(f"{self.name} moved forward.")
    def perform_action(self):
        self.make_sound()
        self.move()
'''
We are creating a subclass(Dog), that inherits the properties and behavior from Animal.
'''

class Dog(Animal):
    def __init__(self,name,sound):
        super().__init__(name,sound)
'''
We are creating a subclass(Cat), that inherits the properties and behavior from Animal.
'''

class Cat(Animal):
    def __init__(self,name,sound):
        super().__init__(name,sound)
dog = Dog("Dog","Woof")

cat = Cat("Cat","Meow")

dog.make_sound()

cat.make_sound()

def do_actions(tAnimal):
    tAnimal.perform_action()
do_actions(dog)

do_actions(cat)

'''
The superclass would be a pencil, and the subclass is a different type of
pencil. The subclass would inherit properties and behavior from pencil, so it
would be similar. The attributes would be how sharp it is, what color it is, and
how long it is. The methods would be sharpening it, the changing the color, and
making it shorter.
'''
class Pencil:
    def __init__(self,sharpness,length):
        self.sharpness = sharpness
        self.length = length
    def sharpen(self,tSharpness):
        print(f"Sharpness was {self.sharpness}.")
        self.sharpness = tSharpness
        print(f"Sharpness is now {self.sharpness}.")
    def change_length(self,tLength):
        print(f"Length was {self.length}.")
        self.length = tLength
        print(f"Length is now {self.length}.")
class Colored_Pencil(Pencil):
    def __init__(self,sharpness,length,color):
        super().__init__(sharpness,length)
        self.color = color
    def change_color(self,tColor):
        print(f"Color was {self.color}")
        self.color = tColor
        print(f"Now {self.color}")
colored_pencil = Colored_Pencil(1,13,"Green.")
colored_pencil.sharpen(5)
colored_pencil.change_length(5)
colored_pencil.change_color("Blue.")



        
        












        
