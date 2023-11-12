import turtle
import random
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(1)
number = random.randint(1,10)
number1 = random.randint(3,8)
def draw():
    for i in range(number):
        for i in range(number1):
            r = random.random()
            g = random.random()
            b = random.random()
            t.color(r,g,b)
            t.forward(random.randint(1,120))
            t.right(random.randint(1,120))
draw()
        
