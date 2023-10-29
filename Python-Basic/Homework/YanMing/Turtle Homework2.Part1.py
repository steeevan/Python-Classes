import turtle
import random
screen = turtle.Screen()
number = random.randint(10,50)
def random_art():
        t = turtle.Turtle()
        for i in range(number):
            numbers = random.randint(1,3)
            r = random.random()
            g = random.random()
            b = random.random()
            t.pencolor(r,g,b)
            if numbers == 1:
                t.penup()
                t.goto(random.randint(0,100),random.randint(0,200))
                t.pendown()
                radius = random.randint(1,100)
                t.circle(radius)
            elif numbers == 2:
                t.penup()
                t.goto(random.randint(0,100),random.randint(0,200))
                t.pendown()
                radius = random.randint(1,100)
                t.forward(radius)
                t.left(120)
                t.forward(radius)
                t.left(120)
                t.forward(radius)
            elif numbers == 3:
                t.penup()
                t.goto(random.randint(0,100),random.randint(0,200))
                t.pendown()
                radius = random.randint(1,100)
                t.forward(radius)
                t.left(90)
                t.forward(radius)
                t.left(90) 
                t.forward(radius) 
                t.left(90)
                t.forward(radius) 
                t.left(90)
            else:
                print("something went wrong")
         
random_art()
turtle.done()
