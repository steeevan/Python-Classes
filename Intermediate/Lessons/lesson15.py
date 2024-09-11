import turtle  # Import the turtle graphics library
import random  # Import the random module for generating random numbers

# Function to draw a random shape
def draw_shape():
    turtle.pendown()  # Lower the pen to start drawing
    # List of possible shapes
    shape_type = ["circle", "square", "triangle", "pentagon", "hexagon", "star"]
    # Select a random shape from the list
    selected_shape = random.choice(shape_type)

    # Draw the selected shape
    if selected_shape == "circle":
        # Draw a circle with a random radius between 10 and 100
        turtle.circle(random.randint(10, 100))
    elif selected_shape == "square":
        # Draw a square with a random side length between 10 and 100
        side_length = random.randint(10, 100)
        for _ in range(4):
            turtle.forward(side_length)
            turtle.right(90)  # Turn 90 degrees to form a square
    elif selected_shape == "triangle":
        # Draw a triangle with a random side length between 10 and 100
        side_length = random.randint(10, 100)
        for _ in range(3):
            turtle.forward(side_length)
            turtle.right(120)  # Turn 120 degrees to form a triangle

    turtle.penup()  # Lift the pen to stop drawing

# Function to move the turtle to a random position
def move_random():
    # Set x and y to random numbers between -200 and 200
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    turtle.penup()  # Lift the pen to avoid drawing while moving
    turtle.goto(x, y)  # Move the turtle to the new position

# Main function to run the entire program
def main():
    turtle.speed(0)  # Set the turtle speed to the fastest
    turtle.hideturtle()  # Hide the turtle cursor
    turtle.bgcolor("black")  # Set the background color to black
    # List of colors to choose from
    colors = ["orange", "blue", "white", "yellow", "green"]

    # Draw 30 shapes at random positions with random colors
    for _ in range(30):
        turtle.color(random.choice(colors))  # Choose a random color
        move_random()  # Move the turtle to a random position
        draw_shape()  # Draw a random shape

    turtle.done()  # Finish the drawing

# Run the main function to start the program
main()
