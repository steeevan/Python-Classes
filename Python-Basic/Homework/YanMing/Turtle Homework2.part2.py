import turtle
import random
screen = turtle.Screen()
def walk():
    t = turtle.Turtle()
    count = 0
    x = int(input("x position? "))
    y = int(input("y position? "))
    t.penup()
    t.goto(x,y)
    t.pendown()
    steps = int(input("How long do you want your turtle to walk? "))
    for i in range(steps):
        angle = random.randint(0,360)
        t.right(angle)
        t.forward(steps)
        count += 1
        print(f"You have walked {count} steps.")
    t.penup()
    t.goto(x,y)
    t.pendown()
    turtle.done()
walk()
