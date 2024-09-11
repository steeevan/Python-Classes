import tkinter as tk
from tkinter import colorchooser  # Import color chooser for selecting brush color

# Create the main application window
root = tk.Tk()  # Initialize the main window
root.title("Simple Drawing App")  # Set the title of the window
root.geometry("800x600")  # Set the dimensions of the window

# Global variables for the brush settings
brush_color = "black"  # Default brush color
brush_size = 5  # Default brush size
animation_speed = 20  # Speed of the drawing refresh rate (lower value = faster refresh)

# Function to change the brush color
def change_color():
    global brush_color
    color = colorchooser.askcolor()[1]  # Open color chooser dialog and get the selected color
    if color:
        brush_color = color  # Update the global brush_color variable

# Function to change the brush size
def change_brush_size(new_size):
    global brush_size
    brush_size = int(new_size)  # Update the global brush_size variable

# Function to clear the canvas
def clear_canvas():
    canvas.delete("all")  # Remove all drawings from the canvas

# Function to draw on the canvas
def paint(event):
    # Calculate the coordinates for the oval based on brush size
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    # Draw an oval on the canvas at the mouse position with the selected brush color and size
    canvas.create_oval(x1, y1, x2, y2, fill=brush_color, outline=brush_color)

# Create the canvas widget
canvas = tk.Canvas(root, bg="white", width=600, height=400)  # Create a white canvas
canvas.pack(pady=20)  # Add the canvas to the window with padding

# Bind the mouse drag event to the paint function
canvas.bind("<B1-Motion>", paint)  # Call paint function when the mouse is dragged on the canvas

# Create a frame to hold the brush options
options_frame = tk.Frame(root)  # Create a frame for options (color, size, clear)
options_frame.pack(pady=30)  # Add the frame to the window with padding

# Brush color button
color_button = tk.Button(options_frame, text="Change Color", command=change_color)  # Button to change brush color
color_button.grid(row=0, column=0, padx=10)  # Place the button in the first column of the frame

# Brush size slider
size_slider = tk.Scale(options_frame, from_=1, to=20, orient=tk.HORIZONTAL, command=change_brush_size)  # Slider for brush size
size_slider.set(brush_size)  # Set the initial value of the slider
size_slider.grid(row=0, column=1, padx=10)  # Place the slider in the second column of the frame

# Clear button
clear_button = tk.Button(options_frame, text="Clear Canvas", command=clear_canvas)  # Button to clear the canvas
clear_button.grid(row=0, column=2, padx=10)  # Place the button in the third column of the frame

# Start the main event loop
root.mainloop()  # Display the window and start handling user events
