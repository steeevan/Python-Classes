class animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
        

    def make_sound(self):
        print(f"name: {self.name} , sound: {self.sound}")
        
    def move(self):
        print("moonwalk")


class dog(animal):
    def __init__(self,name,sound,ss):
        super().__init__(name,sound)
        self.specific_sound = ss

    def dog_sound(self):
        print(f"dog_name: {self.name} , sound: {self.sound} , specific_sound: {self.specific_sound}")


class cat(animal):
    def __init__(self,name,sound,ss):
        super().__init__(name,sound)
        self.specific_sound = ss

    def cat_sound(self):
        print(f"cat_name: {self.name} , sound: {self.sound} , specific_sound: {self.specific_sound}")


def perform_action(tanimal):
    tanimal.make_sound()
    tanimal.move()

animal1 = dog("collie","woof","ungrrrrr")

animal1.make_sound()
animal1.dog_sound()

animal2 = cat("devon rex","meow","urungggg")

animal2.make_sound()
animal2.cat_sound()
perform_action(animal1)
perform_action(animal2)

# real world
class sports_team:
    def __init__(self,name,state):
        self.name = name
        self.state = state

    def display_info(self):
        print(f"name: {self.name} , state: {self.state}")


class basketball_team (sports_team):
    def __init__(self,name,state,city):
        super().__init__(name,state)
        self.city = city

    def display_specific_basketball_info(self):
        print(f"basketball_team: {self.name} , state: {self.state} , city: {self.city}")

class soccer_team (sports_team):
    def __init__(self,name,state,city):
        super().__init__(name,state)
        self.city = city

    def display_specific_soccer_info(self):
        print(f"soccer_team: {self.name} , state: {self.state} , city: {self.city}")

team1 = basketball_team("Golden States Warriors","California","San Francisco")

team1.display_specific_basketball_info()
team1.display_info()

team2 = soccer_team("Los Angeles FC United States","California","Los Angeles")

team2.display_specific_soccer_info()
team2.display_info()
