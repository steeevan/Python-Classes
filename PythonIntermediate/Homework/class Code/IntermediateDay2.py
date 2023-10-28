import turtle
import random

# Create our screen for turtle
screen = turtle.Screen()



# Exercise 1
# Using the code above Create a definition
# named "Spiral" with two parameters
# one named "Distance" and "Angle"
#--------------------------------------------------------
def spiral(Distance,Angle):
     # Create the turtle object
     t = turtle.Turtle()
     t.speed(0)
     t.pensize(3)

     for i in range(100):
          r = random.random()
          g = random.random()
          b = random.random()
          t.pencolor(r,g,b)
          t.forward(Distance)
          t.left(Angle)

     turtle.done()

#spiral(100,123)


# Create a polka dot visual
#-----------------------------------------------------------------
def polka_dot(diameter):
     t= turtle.Turtle()
     t.speed(0)

     for i in range(100):
          x = random.randint(-200,200)
          y = random.randint(-200,200)
          t.penup()
          t.goto(x,y)
          r = random.random()
          g = random.random()
          b = random.random()

          t.pendown()
          t.dot(diameter,(r,g,b))

     turtle.done()

#polka_dot(10)

colors = ["red","blue"]
# Spirograph Art
# Make your turtle
#---------------------------------------------------
def spirograph(diameter,Tlist):
     t  = turtle.Turtle()
     t.speed(0)

     

     for i in range(100):
          t.color(random.choice(Tlist))
          t.pensize(random.randint(1,5))
          t.circle(diameter)
          t.right(10)
     turtle.done()


#spirograph(100,colors)

