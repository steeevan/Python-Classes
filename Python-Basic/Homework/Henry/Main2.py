import turtle
import random
ranges = [10,20,30]
colors = ["red", "white", "blue"]
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(2)
"""
for i in range(10):
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    random.randrange(3,8)
    t.color(random.choice(colors))
    t.forward(random.choice(ranges))
    t.goto(x,y)"""

def RandomPolygon():
    for i in range(10):
        t.pendown()
        t.color(random.choice(colors))
        t.forward(random.randint(10,202))
        t.right(random.randint(20,50))
        t.forward(random.randint(10,35))
        t.left(random.randint(10,75))
        
        t.penup()

for i in range(5):
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    t.goto(x,y)
    RandomPolygon()

RandomPolygon()
turtle.exitonclick()