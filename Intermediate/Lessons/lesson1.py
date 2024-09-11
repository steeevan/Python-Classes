'''
Lesson 1: Turtle Functions
Objective: Review the basics of the Python Turtle library by creating various shapes.

Introduction to Turtle Graphics

Turtle Library Basics:
The Turtle library is a popular way for introducing programming to kids. It provides a virtual canvas where you can draw using a turtle that moves on the screen.
Basic commands:
forward(distance): Move the turtle forward by the specified distance.
backward(distance): Move the turtle backward by the specified distance.
right(angle): Turn the turtle clockwise by the specified angle.
left(angle): Turn the turtle counterclockwise by the specified angle.
penup(): Lift the pen so that moving the turtle does not draw on the canvas.
pendown(): Lower the pen to draw when the turtle moves.
'''

import turtle  # Import the Turtle graphics library for drawing

# Create a turtle object
t = turtle.Turtle()  # Initialize a Turtle object named 't'

# Draw a square
for _ in range(4):  # Repeat 4 times to draw a square
    t.forward(100)  # Move the turtle forward by 100 units
    t.right(90)  # Turn the turtle 90 degrees to the right

# Close the turtle graphics window
turtle.done()  # Finish drawing and close the Turtle graphics window

'''
Activity: Draw a house using basic shapes (square and triangle).
Advanced Shapes and Custom Functions

Creating polygons with a loop:
Using loops, we can create polygons of any number of sides.
'''

import turtle  # Import the Turtle graphics library for drawing

# Create a turtle object
t = turtle.Turtle()  # Initialize a Turtle object named 't'

# Function to draw a polygon with a specified number of sides and length
def draw_polygon(sides, length):
    angle = 360 / sides  # Calculate the angle between sides
    for _ in range(sides):  # Repeat for each side of the polygon
        t.forward(length)  # Move the turtle forward by the specified length
        t.right(angle)  # Turn the turtle by the calculated angle

# Draw a pentagon
draw_polygon(5, 100)  # Call the function to draw a pentagon with 5 sides and length of 100 units

turtle.done()  # Finish drawing and close the Turtle graphics window

'''
Using Pen Colors and Fill Colors

pencolor(color) - Set the color of the pen.
fillcolor(color) - Set the color used to fill shapes.
begin_fill() - Begin filling the shape with the current fill color.
end_fill() - End filling the shape with the current fill color.
'''

import turtle  # Import the Turtle graphics library for drawing

# Create a turtle object
t = turtle.Turtle()  # Initialize a Turtle object named 't'

# Draw a filled star
t.fillcolor("yellow")  # Set the fill color of the star to yellow
t.begin_fill()  # Begin filling the star shape
for _ in range(5):  # Repeat 5 times to draw a star
    t.forward(100)  # Move the turtle forward by 100 units
    t.right(144)  # Turn the turtle 144 degrees to the right (angle to create a star shape)
t.end_fill()  # End filling the star shape

turtle.done()  # Finish drawing and close the Turtle graphics window
