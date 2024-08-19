class animal:
    def __init__(self, name, sound):
        self.name=name
        self.sound=sound
    def make_sound(self, sound):
        print (f'{self.sound}')
    def move(self, place):
        self.place=place
        print (f'moved to {self.place}')
    def perform_action(self, sound, place):
        make_sound(self.sound)
        move(self.place)
        

class dog:
    def __init__(animal, sound):
        sound='Bark'

class cat:
    def __init__(animal, sound):
        sound='mew'

bob=animal.make_sound('Bark')
bob2=animal.make_sound('mew')

animalperform=animal.perform_action('Bark', 'home')

'''
forgot how to use subclasses
'''

'''
Real-world scenario:
if you were to have a pet, they would come under
the class of animal.



'''
















