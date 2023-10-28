import turtle

t = turtle.Turtle()


# square
def square():
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)


# triangle
def triangle():
    for _ in range(3):
        t.forward(100)
        t.left(120)

#cirlce
def circle():
    t.circle(100)
"""
square()
triangle()
circle()"""
"""
def pattern():
    for i in range(10):
        t.right(120)
        t.color("orange")
        t.pendown
        t.forward(75)
        t.left(120)
        t.color("red")
        t.pendown
        t.forward(75)
pattern()
"""

def right():
    t.right(101)

def left():
    t.left(10)

def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)


def Increase_PenSize():
    t.pensize(t.pensize()+1)


def Decrease_PenSize():
    current_size = t.pensize()
    if current_size > 1:
        t.pensize(current_size -1 )

def pen_up():
    t.penup()
def pen_down():
    t.pendown()
    print("down")


def change_Color1():
    t.color("red")
def change_Color2():
    t.color("Yellow")
def change_Color3():
    t.color("Green")





screen = turtle.Screen()
screen.onkey(change_Color1, "1")
screen.onkey(change_Color2, "2")
screen.onkey(change_Color3, "3")
screen.onkey(Increase_PenSize,"plus")
screen.onkey(Decrease_PenSize, "minus")
screen.onkey(move_forward,"Up")
screen.onkey(move_backward,"Down")
screen.onkey(left,"Left")
screen.onkey(right,"Right")
screen.onkey(pen_down,"D")
screen.onkey(pen_up,"U")

screen.listen()
screen.exitonclick()


