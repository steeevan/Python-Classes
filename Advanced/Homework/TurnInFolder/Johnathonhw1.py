class person:
    def __init__(self, name, age, location):
        self.name=name
        self.age=age
        self.location=location
    def greet(self):
        print (f'Hello, my name is {self.name} and I am {self.location}')
    def move(self, location):
        self.location=location
        
someone=person('Johnathon', 12, 'at home')
someone.greet()

#code for scenario
someone_else=person('Jackson', 7, 'at school')
someone_else.greet()

another_guy=person('Kaleo', 12, 'out shopping')
another_guy.greet()
another_guy.move('now driving home')
another_guy.greet()

'''
one real-world scenario is right now... I'm a person,
right? My name is Johnathon, I'm 12 years old, and I'm at
home.
scenario code above ^^^
'''



'''
#1-2
forgot how to initiate a class at some point... :O

#3: very easy, just had to make a real-world scenario
'''



