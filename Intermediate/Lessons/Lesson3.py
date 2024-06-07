import tkinter as tk
from tkinter import colorchooser
import math

# Create the main application window
root = tk.Tk()
root.title("Simple Drawing App")
root.geometry("1000x900")

# Global variables for the brush settings
brush_color = "black"
brush_size = 5
animation_speed = 20  # Decrease this value to speed up the refresh rate

# Settings for simulations
gravity_value = 0.5
pendulum_speed = 1.0

# Function to change the brush color
def change_color():
    global brush_color
    color = colorchooser.askcolor()[1]
    if color:
        brush_color = color

# Function to change the brush size
def change_brush_size(new_size):
    global brush_size
    brush_size = int(new_size)

# Function to change gravity
def change_gravity(new_gravity):
    global gravity_value
    gravity_value = float(new_gravity)

# Function to change pendulum speed
def change_pendulum_speed(new_speed):
    global pendulum_speed
    pendulum_speed = float(new_speed)

# Function to draw on the canvas
def paint(event):
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    canvas.create_oval(x1, y1, x2, y2, fill=brush_color, outline=brush_color)

# Function to clear the canvas
def clear_canvas():
    canvas.delete("all")

# Function to create a simple animation
def create_animation():
    canvas.delete("all")
    ball = canvas.create_oval(10, 10, 50, 50, fill="blue")
    move_ball(ball)

def move_ball(ball):
    canvas.move(ball, 5, 0)
    canvas.update()
    canvas.after(animation_speed, move_ball, ball)

# Function to create a bouncing ball animation
def create_bouncing_ball():
    canvas.delete("all")
    ball = canvas.create_oval(10, 10, 50, 50, fill="red")
    move_bouncing_ball(ball, 5, 5)

def move_bouncing_ball(ball, dx, dy):
    coords = canvas.coords(ball)
    if coords[2] >= canvas.winfo_width() or coords[0] <= 0:
        dx = -dx
    if coords[3] >= canvas.winfo_height() or coords[1] <= 0:
        dy = -dy
    canvas.move(ball, dx, dy)
    canvas.update()
    canvas.after(animation_speed, move_bouncing_ball, ball, dx, dy)

# Function to create an expanding circle animation
def create_expanding_circle():
    canvas.delete("all")
    circle = canvas.create_oval(300, 200, 350, 250, fill="green")
    expand_circle(circle, 1, True)

def expand_circle(circle, size, expanding):
    coords = canvas.coords(circle)
    if coords[2] - coords[0] >= 200:
        expanding = False
    elif coords[2] - coords[0] <= 50:
        expanding = True
    
    scale = 1 + size / 50.0 if expanding else 1 - size / 50.0
    canvas.scale(circle, 325, 225, scale, scale)
    canvas.update()
    canvas.after(animation_speed, expand_circle, circle, size, expanding)

# Function to create a moving square animation
def create_moving_square():
    canvas.delete("all")
    square = canvas.create_rectangle(10, 10, 50, 50, fill="yellow")
    move_square(square, 5, 5)

def move_square(square, dx, dy):
    coords = canvas.coords(square)
    if coords[2] >= canvas.winfo_width() or coords[0] <= 0:
        dx = -dx
    if coords[3] >= canvas.winfo_height() or coords[1] <= 0:
        dy = -dy
    canvas.move(square, dx, dy)
    canvas.update()
    canvas.after(animation_speed, move_square, square, dx, dy)

# Function to create a gravity simulation
def create_gravity_simulation():
    canvas.delete("all")
    ball = canvas.create_oval(200, 200, 250, 250, fill="purple")
    simulate_gravity(ball, 0, gravity_value)

def simulate_gravity(ball, dy, gravity):
    coords = canvas.coords(ball)
    if coords[3] >= canvas.winfo_height() and dy > 0:
        dy = -dy * 0.9
    else:
        dy += gravity
    canvas.move(ball, 0, dy)
    canvas.update()
    canvas.after(animation_speed, simulate_gravity, ball, dy, gravity)

# Function to create a pendulum simulation
def create_pendulum_simulation():
    canvas.delete("all")
    length = 200
    origin_x = canvas.winfo_width() // 2
    origin_y = 50
    ball_x = origin_x + length * math.sin(math.pi / 4)
    ball_y = origin_y + length * math.cos(math.pi / 4)
    rod = canvas.create_line(origin_x, origin_y, ball_x, ball_y, width=2)
    ball = canvas.create_oval(ball_x - 20, ball_y - 20, ball_x + 20, ball_y + 20, fill="orange")
    simulate_pendulum(rod, ball, origin_x, origin_y, length, math.pi / 4, 0, pendulum_speed)

def simulate_pendulum(rod, ball, origin_x, origin_y, length, angle, angular_velocity, speed):
    gravity = 0.01 * speed
    angular_acceleration = -gravity * math.sin(angle)
    angle += angular_velocity
    angular_velocity += angular_acceleration
    angular_velocity *= 0.99  # damping
    ball_x = origin_x + length * math.sin(angle)
    ball_y = origin_y + length * math.cos(angle)
    canvas.coords(rod, origin_x, origin_y, ball_x, ball_y)
    canvas.coords(ball, ball_x - 20, ball_y - 20, ball_x + 20, ball_y + 20)
    canvas.update()
    canvas.after(animation_speed, simulate_pendulum, rod, ball, origin_x, origin_y, length, angle, angular_velocity, speed)

# Create the canvas widget
canvas = tk.Canvas(root, bg="white", width=600, height=400)
canvas.pack(pady=20)

# Bind the mouse drag event to the paint function
canvas.bind("<B1-Motion>", paint)

# Create a frame to hold the brush options
options_frame = tk.Frame(root)
options_frame.pack(pady=20)

# Brush color button
color_button = tk.Button(options_frame, text="Change Color", command=change_color)
color_button.grid(row=0, column=0, padx=10)

# Brush size slider
size_slider = tk.Scale(options_frame, from_=1, to=20, orient=tk.HORIZONTAL, command=change_brush_size)
size_slider.set(brush_size)
size_slider.grid(row=0, column=1, padx=10)

# Clear canvas button
clear_button = tk.Button(options_frame, text="Clear Canvas", command=clear_canvas)
clear_button.grid(row=0, column=2, padx=10)

# Animation buttons
animation_button = tk.Button(options_frame, text="Horizontal Ball Animation", command=create_animation)
animation_button.grid(row=0, column=3, padx=10)

bouncing_ball_button = tk.Button(options_frame, text="Bouncing Ball Animation", command=create_bouncing_ball)
bouncing_ball_button.grid(row=1, column=0, padx=10, pady=10)

expanding_circle_button = tk.Button(options_frame, text="Expanding Circle Animation", command=create_expanding_circle)
expanding_circle_button.grid(row=1, column=1, padx=10, pady=10)

moving_square_button = tk.Button(options_frame, text="Moving Square Animation", command=create_moving_square)
moving_square_button.grid(row=1, column=2, padx=10, pady=10)

gravity_simulation_button = tk.Button(options_frame, text="Gravity Simulation", command=create_gravity_simulation)
gravity_simulation_button.grid(row=1, column=3, padx=10, pady=10)

pendulum_simulation_button = tk.Button(options_frame, text="Pendulum Simulation", command=create_pendulum_simulation)
pendulum_simulation_button.grid(row=1, column=4, padx=10, pady=10)

# Sliders for gravity and pendulum speed
gravity_slider = tk.Scale(options_frame, from_=0.1, to=2.0, resolution=0.1, orient=tk.HORIZONTAL, label="Gravity", command=change_gravity)
gravity_slider.set(gravity_value)
gravity_slider.grid(row=2, column=0, columnspan=2, pady=10)

pendulum_speed_slider = tk.Scale(options_frame, from_=0.5, to=3.0, resolution=0.1, orient=tk.HORIZONTAL, label="Pendulum Speed", command=change_pendulum_speed)
pendulum_speed_slider.set(pendulum_speed)
pendulum_speed_slider.grid(row=2, column=2, columnspan=2, pady=10)

# Start the main event loop
root.mainloop()
