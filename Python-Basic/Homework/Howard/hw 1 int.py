
# exercise 1


def square():
    import turtle

    t = turtle.Turtle()

    screen = turtle.Screen()

    screen.bgcolor("light blue")

    t.speed(1)

    t.pencolor("red")
    t.pensize(5)
    t.fillcolor("pink")
    t.begin_fill()
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.end_fill()

def triangle():
    import turtle

    t = turtle.Turtle()

    screen = turtle.Screen()

    screen.bgcolor("light blue")

    t.speed(1)

    t.pencolor("red")
    t.pensize(5)
    t.fillcolor("purple")
    t.begin_fill()
    t.right(30)
    t.pencolor("teal")
    t.forward(100)
    t.right(120)
    t.pencolor("pink")
    t.forward(100)
    t.right(120)
    t.pencolor("black")
    t.forward(100)
    t.end_fill()

def circle():
    import turtle

    t = turtle.Turtle()

    screen = turtle.Screen()

    screen.bgcolor("light blue")

    t.speed(1)

    t.pencolor("red")
    t.pensize(5)
    t.pencolor("blue")
    t.pensize(5)

    t.fillcolor("green")
    t.begin_fill()
    t.circle(50)
    t.end_fill()

# exercise 2
def draw_tank(pen_color, size, startX, startY):
    import turtle
    t = turtle.Turtle()
    screen = turtle.Screen()
    t.speed(5)
    t.penup()
    t.goto(startX,startY)
    t.pendown()

    t.pencolor(pen_color)
    t.pensize(1)

    t.fillcolor("gray")
    t.begin_fill()
    t.circle(10 * size)
    t.end_fill()
    t.fillcolor("green")
    t.begin_fill()
    t.forward(100 * size)
    t.begin_fill()
    t.circle(10 * size)
    t.end_fill()
    t.left(90)
    t.penup()
    t.forward(20 * size)
    t.pendown()
    t.left(90)
    t.forward(100 * size)
    t.right(120)
    t.forward(20 * size)
    t.right(60)
    t.forward(80 * size)
    t.right(60)
    t.forward(20 * size)
    t.penup()
    t.right(120)
    t.forward(100 * size)
    t.right(120)
    t.forward(20 * size)
    t.right(60)
    t.pendown()
    t.forward(20 * size)
    t.left(90)
    t.forward(20 * size)
    t.right(90)
    t.forward(40 * size)
    t.right(90)
    t.forward(20 * size)
    t.left(180)
    t.forward(9 * size)
    t.right(90)
    t.forward(50 * size)
    t.left(90)
    t.forward(2 * size)
    t.left(90)
    t.forward(50 * size)
    t.left(180)
    t.forward(50 * size)
    t.end_fill()

def more_tanks():
    for i in range(1,1000000):
        draw_tank("green",0.5+0.5*i,-25*i,-25*i+150)

# PROBLEM 3 
def tank_spot():
    import turtle
    def get_mouse_click_coor(x, y):
        draw_tank("blue",1,x,y)
        
    turtle.onscreenclick(get_mouse_click_coor)

    turtle.mainloop()

