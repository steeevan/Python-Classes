import turtle  # Import the turtle graphics library
import random  # Import the random library for generating random numbers
import tkinter as tk  # Import the tkinter library for the GUI

# List to hold turtle objects
turtles = []
# Define the position of the finish line
finish_line = 200

# Function to move a turtle forward by a random distance
def move_turtle(turtle_obj):
    distance = random.randint(1, 50)  # Generate a random distance between 1 and 50
    turtle_obj.forward(distance)  # Move the turtle forward by the generated distance

# Function to check if a turtle has reached the finish line
def has_reached_finish_line(turtle_obj, finish_line):
    return turtle_obj.xcor() >= finish_line  # Return True if the turtle's x-coordinate is greater than or equal to the finish line

# Function to get user input for the race
def get_racers():
    num_turtle = int(input("Enter the amount of turtles in the race: "))  # Get the number of turtles from the user

    # Set up the turtle graphics
    turtle.speed(2)  # Set the turtle speed
    turtle.hideturtle()  # Hide the default turtle
    turtle.penup()  # Lift the pen to avoid drawing lines

    # Create the turtles and set their initial starting positions
    for i in range(num_turtle):
        chicken = turtle.Turtle()  # Create a new turtle object
        chicken.shape("turtle")  # Set the shape of the turtle
        chicken.color(random.random(), random.random(), random.random())  # Set the turtle's color to a random color
        chicken.penup()  # Lift the pen to avoid drawing lines
        chicken.goto(-200, -150 + i * 50)  # Set the turtle's starting position with spacing
        turtles.append(chicken)  # Add the turtle to the list of turtles

# Function to start the race
def start_race():
    winner = None  # Initialize the winner variable
    while not winner:  # Continue racing until a winner is found
        for c in turtles:
            move_turtle(c)  # Move each turtle
            if has_reached_finish_line(c, finish_line):  # Check if the turtle has reached the finish line
                winner = c  # Set the winner to the turtle that reached the finish line
                break  # Exit the loop if a winner is found

    # Display the winner
    turtle.goto(0, 0)  # Move to the center of the screen
    turtle.color("black")  # Set the turtle's color for writing
    turtle.write(f"The winner is Turtle {turtles.index(winner) + 1}!", align="center", font=("Arial", 24, "normal"))  # Write the winner's information

# Create the Tkinter GUI window
root = tk.Tk()
root.title("Turtle Race")  # Set the title of the window

# Button to start the race
start_button = tk.Button(root, text="Start Race", command=start_race)  # Create a button to start the race
start_button.pack(pady=20)  # Add the button to the window

# Get the number of turtles from the user
get_racers()

# Start the Tkinter event loop
root.mainloop()
turtle.exitonclick()  # Exit on clicking the turtle graphics window
