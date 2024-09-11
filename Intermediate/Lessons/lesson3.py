'''
Lesson 3: Turtle and Math
Objective: Utilize the Math library to model mathematical concepts and recursive algorithms.

Introduction to the Math Library

Using math functions:
math.sin(x), math.cos(x): Return the sine and cosine of x (in radians).
math.pi: The mathematical constant π.
'''
import turtle  # Import the turtle graphics library for drawing
import math  # Import the math library for mathematical functions

# Create a turtle object
t = turtle.Turtle()  # Initializes a turtle object for drawing

# Draw a sine wave
t.penup()  # Lift the pen to move the turtle without drawing
t.goto(-360, 0)  # Move the turtle to the starting point of the sine wave
t.pendown()  # Lower the pen to start drawing
for x in range(-360, 361):  # Iterate through x values from -360 to 360
    y = math.sin(math.radians(x)) * 100  # Calculate y using the sine of x (converted to radians) scaled by 100
    t.goto(x, y)  # Move the turtle to the new (x, y) position to draw the wave

turtle.done()  # Finish the turtle drawing and close the window

'''
Recursive Algorithms with Turtle

Introduction to recursion:
Recursion is a method of solving a problem where the solution depends on solutions to smaller instances of the same problem.
'''
import turtle  # Import the turtle graphics library for drawing

# Create a turtle object
t = turtle.Turtle()  # Initializes a turtle object for drawing

# Function to draw a fractal tree
def draw_tree(branch_length):
    if branch_length > 5:  # Base case: stop recursion when branch length is too short
        t.forward(branch_length)  # Draw the current branch
        t.right(20)  # Turn right to draw the right subtree
        draw_tree(branch_length - 15)  # Recursively draw the right subtree with shorter branches
        t.left(40)  # Turn left to draw the left subtree
        draw_tree(branch_length - 15)  # Recursively draw the left subtree with shorter branches
        t.right(20)  # Restore the original orientation
        t.backward(branch_length)  # Move the turtle back to the starting point of the branch

# Set up the initial position and orientation for drawing
t.left(90)  # Turn the turtle to face upwards
t.penup()  # Lift the pen to move the turtle without drawing
t.goto(0, -200)  # Move the turtle to the starting position for the tree
t.pendown()  # Lower the pen to start drawing

draw_tree(100)  # Start drawing the fractal tree with initial branch length of 100

turtle.done()  # Finish the turtle drawing and close the window
