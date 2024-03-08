#problem 1 and 2

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"this animal makes the sound {self.sound}")

    def move(self):
        print(f"the animal is moving to a better place")

    def preform_action(self, Animal):
        print(f"this animal is making {self.sound} noises while moving to a better place")
        
        


Dog = Animal("dog", "roof")
cat = Animal("cat", "meow")

Dog.make_sound
cat.make_sound
Dog.move
cat.move
Dog.preform_action
cat.preform_action
#Problem 3

class inherit:
    def __init__(self, item, money, name):
        self.item = item
        self.money = money
        self.name = name

    def death(self):
        print(f"this person took {self.name}'s {self.item} and got {self.money}$ since he inherited from {self.name}")
        

    def life(self):
        print(f" this person could not inherit from {self.name} because he is alive")

    def life_and_death(self):
        print(f" this person could not inherit from {self.name} because he is alive but right now you can take {self.name}'s {self.item} and get {self.money}$ since im nice")


person1 = inherit("used tissue", 1, "Hubert Blaine Wolfeschlegelsteinhausenbergerdorff Sr.")
person2 = inherit("mansion", 64289731642873164218736487312,"Harper")
person1.death
person2.death
person1.life
person2.life
person1.life_and_death
person2.life_and_death
