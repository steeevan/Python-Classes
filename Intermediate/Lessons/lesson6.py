'''
Lesson 6: Tkinter Movement
Objective: Use Tkinter to create an interactive Pong game.

Drawing and Moving Shapes in Tkinter

Creating a canvas:
Canvas widget is used to draw shapes.
'''

import tkinter as tk  # Import the Tkinter library for creating GUI applications

# Create the main window
root = tk.Tk()  # Initialize the main application window
root.title("Animation")  # Set the title of the main window

# Create a canvas widget for drawing shapes
canvas = tk.Canvas(root, width=400, height=400)  # Create a Canvas widget with specified width and height
canvas.pack()  # Add the Canvas widget to the window

# Draw a rectangle on the canvas
rect = canvas.create_rectangle(50, 50, 100, 100, fill="blue")  # Draw a blue rectangle at specified coordinates

# Function to move the rectangle
def move_rect():
    canvas.move(rect, 5, 0)  # Move the rectangle 5 pixels to the right (x direction)
    root.after(50, move_rect)  # Schedule the move_rect function to be called again after 50 milliseconds

move_rect()  # Start moving the rectangle

# Run the application
root.mainloop()  # Start the Tkinter event loop to display the window and handle user interactions

'''
Creating the Pong Game

Setting up the game window and canvas:
Create paddles and ball.
Implement game mechanics: paddle movement, ball bouncing.
'''

import tkinter as tk  # Import the Tkinter library for creating GUI applications

# Create the main window
root = tk.Tk()  # Initialize the main application window
root.title("Pong Game")  # Set the title of the main window

# Create a canvas widget for the game
canvas = tk.Canvas(root, width=800, height=400, bg="black")  # Create a Canvas widget with a black background
canvas.pack()  # Add the Canvas widget to the window

# Create paddles and a ball
paddle1 = canvas.create_rectangle(30, 150, 50, 250, fill="white")  # Create the left paddle
paddle2 = canvas.create_rectangle(750, 150, 770, 250, fill="white")  # Create the right paddle
ball = canvas.create_oval(390, 190, 410, 210, fill="white")  # Create the ball

# Variables for ball movement
ball_dx = 3  # Speed of the ball in the x direction
ball_dy = 3  # Speed of the ball in the y direction

# Function to move paddles based on key presses
def move_paddle(event):
    key = event.keysym  # Get the key that was pressed
    if key == "w":
        canvas.move(paddle1, 0, -20)  # Move the left paddle up
    elif key == "s":
        canvas.move(paddle1, 0, 20)  # Move the left paddle down
    elif key == "Up":
        canvas.move(paddle2, 0, -20)  # Move the right paddle up
    elif key == "Down":
        canvas.move(paddle2, 0, 20)  # Move the right paddle down

# Bind key presses to the move_paddle function
canvas.bind_all("<KeyPress>", move_paddle)  # Bind all key presses to the move_paddle function

# Function to move the ball and handle collisions
def move_ball():
    global ball_dx, ball_dy  # Declare ball_dx and ball_dy as global variables
    canvas.move(ball, ball_dx, ball_dy)  # Move the ball by ball_dx and ball_dy
    ball_pos = canvas.coords(ball)  # Get the current position of the ball
    # Check for collision with top or bottom edges of the canvas
    if ball_pos[1] <= 0 or ball_pos[3] >= 400:
        ball_dy = -ball_dy  # Reverse the ball's y direction
    # Check for collision with left or right edges of the canvas
    if ball_pos[0] <= 0 or ball_pos[2] >= 800:
        ball_dx = -ball_dx  # Reverse the ball's x direction
    root.after(50, move_ball)  # Schedule the move_ball function to be called again after 50 milliseconds

move_ball()  # Start moving the ball

# Run the application
root.mainloop()  # Start the Tkinter event loop to display the window and handle user interactions
