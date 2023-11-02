import turtle
import random
t = turtle.Turtle()

screen = turtle.Screen()
colors = ["Red", "blue", "green", "Purple"]



def circle():
    t.pendown()
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    t.goto(x,y)
    t.pensize(random.randint(10,20))
    for i in range(4):
        t.color(random.choice(colors))
    t.circle(100)
    t.penup()
    
    

def square():
    t.pendown()
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    t.goto(x,y)
    t.pensize(random.randint(10,20))
    for i in range(4):
        t.color(random.choice(colors))
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.penup()

def triangle():
    t.pendown()
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    t.goto(x,y)

    t.pensize(random.randint(10,20))
    for i in range(4):
        t.color(random.choice(colors))
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.penup()
    


    
my_list = [triangle,square,circle]

for i in range(10):
    ranFunction  = random.choice(my_list)
    ranFunction()
