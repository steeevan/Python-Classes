'''
Lesson 2: Turtle and Random
Objective: Learn to create spirographs and intricate drawings with Turtle and the Random library.

Introduction to the Random Library

Generating random numbers:
random.randint(a, b): Return a random integer N such that a <= N <= b.
random.choice(sequence): Return a randomly chosen element from a non-empty sequence.
'''
import turtle  # Import the turtle graphics library for drawing
import random  # Import the random library to generate random numbers

# Create a turtle object
t = turtle.Turtle()  # Initializes a turtle object for drawing

# Random walk
for _ in range(100):
    t.forward(30)  # Move the turtle forward by 30 units
    t.right(random.randint(0, 360))  # Turn the turtle right by a random angle between 0 and 360 degrees

turtle.done()  # Finish the turtle drawing and close the window

'''
Creating Spirographs

Understanding spirographs and their mathematical basis:
A spirograph is a geometric drawing that produces a curve known as a hypotrochoid.
Using loops and turtle, we can create these intricate designs.
'''
import turtle  # Import the turtle graphics library for drawing
import random  # Import the random library to generate random colors

# Create a turtle object
t = turtle.Turtle()  # Initializes a turtle object for drawing
t.speed(0)  # Set the turtle's drawing speed to the fastest

# Function to draw a spirograph
def draw_spirograph(size):
    # Draw a spirograph by repeatedly drawing circles and rotating
    for _ in range(int(360 / size)):  # Repeat enough times to complete a full spirograph pattern
        t.pencolor(random.choice(['red', 'green', 'blue', 'yellow', 'purple']))  # Choose a random color for the pen
        t.circle(100)  # Draw a circle with radius 100 units
        t.right(size)  # Rotate the turtle right by the specified angle

draw_spirograph(10)  # Call the function to draw a spirograph with a rotation size of 10 degrees

turtle.done()  # Finish the turtle drawing and close the window
