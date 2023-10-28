import turtle

# set up the turtle object
t = turtle.Turtle()

# Create a screen object
screen = turtle.Screen()

# Set the background color of the screen
screen.bgcolor("beige")

# Set the turtle speed ( 0 is fastest, 1-10)
t.speed(1)

# Moves turtle foward
t.forward(100)

# Move turtle backwards
# Turn the turtle to the left
t.left(90)

# Turn the turtle to the right
t.right(90)


# make a square
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
#----------------------------------
# Change color of pen
t.pencolor("red")
t.pensize(5)
#draw a circle
t.circle(50)

# Draw my square with different colors
t.fillcolor("green")
t.begin_fill()
t.right(90)
t.penup()

t.forward(100)
t.right(90)
t.pendown()
t.forward(100)
t.penup()
t.right(90)
t.forward(100)
t.pendown()
t.right(90)
t.forward(100)
t.end_fill()
'''
# Draw a triangle
t.begin_fill()
t.fillcolor("Red")
t.pencolor("Black")
t.pendown()
t.right(60)
t.forward(100)


t.pencolor("Green")
t.pendown()
t.right(60)
t.forward(100)


t.pencolor("Pink")
t

t.left(60)
t.forward(100)

t.end_fill()

'''


def my_square(size_length):
    for i in range(4):
          t.forward(size_length)
          t.right(90)

my_square(10)


 


