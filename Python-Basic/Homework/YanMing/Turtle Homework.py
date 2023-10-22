import turtle
import colorsys
turtle = turtle.Turtle()
turtle.pencolor("green")
turtle.pensize(2)
for i in range(4):
    turtle.forward(50)
    turtle.right(90)
turtle.forward(100)
for i in range(2):
    turtle.left(120)
    turtle.forward(100)
turtle.circle(100)
#--------------------
h = 0
for i in range(460):
    c = colorsys.hsv_to_rgb(h,1,0.9)
    h+=1/36
    turtle.color(c)
    turtle.left(145)
    for j in range(5):
        turtle.forward(300)
        turtle.left(150)
