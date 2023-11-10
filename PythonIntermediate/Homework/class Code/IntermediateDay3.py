
'''
- Combining the Turtle and Math modules in Python allows for creative visualization of mathematical concepts.
- Turtle provides a graphics environment for drawing shapes and patterns, while Math offers mathematical functions.
- This combination enables the creation of geometric patterns, fractals, and mathematical art.
- It is a valuable educational tool for teaching geometry, trigonometry, and calculus interactively.
- The integration encourages hands-on exploration of complex mathematical principles through programming and artistic expression.
'''
import turtle
import math

# Drawing a Circle

# Initialize the Turtle screen
screen = turtle.Screen()
t = turtle.Turtle()

# Draw a circle
radius = 100
t.circle(radius)

# Close the screen on click
screen.exitonclick()
#---------------------------------------------


# Drawing a Spiral

# Initialize the Turtle screen
screen = turtle.Screen()
t = turtle.Turtle()

# Draw a spiral
for i in range(360):
    t.forward(10)
    t.right(math.sin(math.radians(i)) * 20)

# Close the screen on click
screen.exitonclick()
#---------------------------------------------

#Drawing a Sine Wave

# Initialize the Turtle screen
screen = turtle.Screen()
t = turtle.Turtle()

# Draw a sine wave
amplitude = 100
frequency = 1
for x in range(360):
    y = amplitude * math.sin(math.radians(frequency * x))
    t.goto(x, y)

# Close the screen on click
screen.exitonclick()


#---------------------------------------------

# Drawing a Spirograph

# Initialize the Turtle screen
screen = turtle.Screen()
t = turtle.Turtle()

# Draw a spirograph
R = 100
r = 50
d = 50
angle = 0
for _ in range(360):
    x = (R - r) * math.cos(math.radians(angle)) + d * math.cos(((R - r) / r) * math.radians(angle))
    y = (R - r) * math.sin(math.radians(angle)) - d * math.sin(((R - r) / r) * math.radians(angle))
    t.goto(x, y)
    angle += 5

# Close the screen on click
screen.exitonclick()



#---------------------------------------------


# Drawing a flower

# Initialize the Turtle screen
screen = turtle.Screen()
t = turtle.Turtle()

# Draw a flower
petal_length = 100
num_petals = 6
angle = 360 / num_petals

for _ in range(num_petals):
    t.circle(petal_length, 60)
    t.left(120)
    t.circle(petal_length, 60)
    t.left(120)
    t.left(angle)

# Close the screen on click
screen.exitonclick()


#-------------------------------------------

# Drawing a star
# Initialize the Turtle screen
screen = turtle.Screen()
t = turtle.Turtle()

# Draw a star
side_length = 200
angle = 144

for _ in range(5):
    t.forward(side_length)
    t.right(angle)

# Close the screen on click
screen.exitonclick()

#-------------------------------------------
# Drawing a snowflake
import turtle
import math

# Initialize the Turtle screen
screen = turtle.Screen()
t = turtle.Turtle()

# Draw a snowflake
def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)

for _ in range(3):
    koch_snowflake(t, 4, 300)
    t.right(120)

# Close the screen on click
screen.exitonclick()


