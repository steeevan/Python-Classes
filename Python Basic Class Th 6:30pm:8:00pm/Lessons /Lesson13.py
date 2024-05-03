# ===============================================
# Lesson Plan: Turtle Module / Random Module in Python
# ===============================================

# **Objective:** Introduce a module that allows them to draw using Python.
#Learn various methods that can be used to achieve this. 
#Introduction to a module that allows data to be randomly generated, sorted, and more. Here they will
#learn how to create data sets using the module.

# ===============================================
# 1. Introduction to the Turtle Module
# ===============================================

# The Turtle module in Python provides a simple and
# interactive way to create drawings and graphics.

import turtle as tk

# Create a turtle screen and turtle object
screen = tk.Screen()
myTurtle = tk.Turtle()
#piwexls width/height
screen.setup(width=800,height=600)

myTurtle.shape("turtle")
# ===============================================
# 2. Basic Turtle Graphics
# ===============================================

# Explore basic Turtle graphics commands for drawing lines and shapes.

myTurtle.forward(100)
myTurtle.left(90)
myTurtle.circle(50)


# ===============================================
# 3. Random Data Generation with the Random Module
# ===============================================

# The Random module in Python allows you to generate random data, shuffle sequences, and more.
import random
 
#Generate a random integer
random_integer = random.randint(1,10)

# Shiffle a l list
myList = [1,2,3,4,5]
random.shuffle(myList)

# ===============================================
# 4. Drawing Shapes with Turtle
# ===============================================

# Explore drawing shapes and patterns using Turtle graphics.

for i in range(4):
  myTurtle.forward(100)
  myTurtle.right(90)
  
# Draw a colorful start
myTurtle.width(2)
colors = ["red","green", "blue","orange","purple"]
for i in range(5):
  myTurtle.color(random.choice(colors))
  myTurtle.forward(100)
  myTurtle.right(144)


myTurtle.clear()
# setting speed for turtle
myTurtle.speed(0)
# set the initial value
radius = 5

#number of circles
num_circles = 50
angle = 360 / num_circles

for i in range(num_circles):
  myTurtle.color(random.choice(colors))

  myTurtle.circle(radius)
  myTurtle.penup()
  myTurtle.goto(0,0)
  myTurtle.pendown()
  radius += 10
  
  myTurtle.right(angle)
  
  
  
myTurtle.clear()

radius = 10
angle = 90
# Draw a colorful spiral
for i in range(100):
    # Generate a random color
    color = (random.random(), random.random(), random.random())
    # Set the pen color
    myTurtle.pencolor(color)
    # Draw a circle with the current radius
    myTurtle.circle(radius)
    # Increase the radius and decrease the angle
    radius += 5
    angle -= 1
  
  




screen.mainloop()


















  
  
  
  
  
  
  











# ===============================================
# 7. Conclusion
# ===============================================

# In this lesson, you've learned about the Turtle module for drawing graphics in Python and the Random module for generating random data. Turtle graphics allow you to create interactive drawings and patterns, while the Random module is useful for various tasks like data generation and shuffling.

# Continue exploring these modules to enhance your creativity and data manipulation skills in Python.

# ===============================================
# Vocabulary Words and Definitions
# ===============================================

# - Turtle Module: A Python module that provides a simple way to create drawings and graphics.
# - Random Module: A Python module that allows you to generate random data, shuffle sequences, and perform other random-related tasks.
# - Shuffle: To randomize the order of elements in a sequence.















