
import turtle
import random

# Function to draw a random shape
# The purpose of this is to pick any shape then based
# on the picked shape, it draws it.

def draw_shape():
  turtle.pendown()
  shape_type = ["circle","square",'triangle']
  Rshape = random.choice(shape_type)
  
  if Rshape == "circle":
    turtle.circle(random.randint(10,100))
  elif Rshape == "square":
    side_length = random.randint(20,100)
    for _ in range(4):
      turtle.forward(side_length)
      turtle.right(90)
  elif Rshape == "triangle":
    side_length = random.randint(20,100)
    for _ in range(3):
      turtle.forward(side_length)
      turtle.right(120)
  turtle.penup()
  
# This function will move the pen randomly acroos the screen
def move_random():
  # set x and y to random number between [-200,200]
  x = random.randint(-200,200)
  y = random.randint(-200,200)
  turtle.penup()
  turtle.goto(x,y)
  
def main():
  turtle.speed(0) # sets the turtle speed to fastest
  turtle.hideturtle() # hide the turtle icon
  turtle.bgcolor("black") # sets the background color
  colors = ["red",'orange',"yellow","green","blue","purple","white"]
  
  for _ in range(50):
    turtle.color(random.choice(colors))
    move_random()
    draw_shape()
    
    
  turtle.done()

main()
  
  
  
  
