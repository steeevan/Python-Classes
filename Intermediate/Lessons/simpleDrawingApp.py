'''
Day 3 Intermediate Python working with Tkinter

Warm up Exercise:
1. You must prompt the user to enter their full name and
store it into a variable 'name'.
2. Create a window of size 800 by 800.
3. Create a label that displays the variable 'name'
4. Change background color to any color you want.
'''
import tkinter as tk
from tkinter import colorchooser

# Create the main application window
root = tk.Tk()
root.title("Drawing App")
root.geometry("800x600")

# Global variables for the brush settings
brush_color = "black"
brush_size = 5

# function to change the brush color
def change_color():
    global brush_color
    color = colorchooser.askcolor()[1]
    if color:
        brush_color = color

# Function to change the size of the brush
def change_brush_size(new_size):
    global brush_size
    brush_size = int(new_size)

# Function to draw on the canvas
def paint(event):
    x1, y1 = (event.x - brush_size),(event.y - brush_size)
    x2, y2 = (event.x + brush_size),(event.y + brush_size)
    canvas.create_oval(x1,y1,x2,y2,fill=brush_color, outline=brush_color)

# Function to clear the canvas
def clear_canvas():
    canvas.delete("all")

# Create the canvas widget
canvas = tk.Canvas(root, bg="white", width = 600, height = 400)
canvas.pack(pady=20)

# Bind the mouse drag event to the paint function
canvas.bind("<B1-Motion>",paint)

# Create a frame to hold the brush options
options_frame = tk.Frame(root)
options_frame.pack(pady=20)

# Brush Color button
color_button = tk.Button(options_frame, text="Change color", command= change_color)
color_button.grid(row=0,column=0,padx=10)

# Brush size slider
size_slider = tk.Scale(options_frame, from_=1, to=20,orient= tk.HORIZONTAL, command=change_brush_size)
size_slider.set(brush_size)
size_slider.grid(row = 0, column = 1, padx = 10)

# Clear canvas button
clear_button = tk.Button(options_frame, text="Clear Canvas", command= clear_canvas)
clear_button.grid(row = 0, column = 2, padx = 10)

root.mainloop()





















    





    






    
