#question 1
import turtle
import random
t = turtle.Turtle()
t.speed(0)

def square():
    size = random.randrange(50,300)
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(4):
        r = random.random()
        g = random.random()
        b = random.random()
        t.pencolor(r,g,b)
        t.forward(size)
        t.right(90)


def triangle():
    size = random.randrange(50,300)
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(3):
        r = random.random()
        g = random.random()
        b = random.random()
        t.pencolor(r,g,b)
        t.forward(size)
        t.right(120)


def circle():
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    t.penup()
    t.goto(x,y)
    t.pendown()
    size = random.randrange(50,300)
    r = random.random()
    g = random.random()
    b = random.random()
    t.pencolor(r,g,b)
    t.circle(size)
   

def random_times():
    times = random.randint(10,50)
    shapes = [triangle, square, circle]
    for i in range(1,times):
        random.choice(shapes)()

#question 2
def walk():
    size = random.randrange(50,300)
    x = random.randint(-100,100)
    y = random.randint(-100,100)
    t.penup()
    t.goto(x,y)
    t.pendown()
    inn = int(input("input the number of steps that you want the turtle to take: "))
    total = 0
    for i in range(inn):
        length = random.randrange(50,100)
        t.right(random.randrange(0,360))
        t.forward(length)
        total = (length + total)
        print(total)
    t.goto(x,y)
    print("the total distance the turtle has traveled is ",total)
