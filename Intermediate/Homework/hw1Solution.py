import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Change Background Color")
root.geometry("300x200")

# Function to change the background color
def change_bg_color():
    selected_color = color_var.get()
    root.configure(bg=selected_color)

# Create a StringVar to hold the selected color
color_var = tk.StringVar(value="Select a color")

# Create a dropdown menu (OptionMenu) for color selection
colors = ["red", "green", "blue", "yellow", "white", "black"]
color_menu = tk.OptionMenu(root, color_var, *colors, command=lambda _: change_bg_color())
color_menu.pack(pady=20)

# Start the main event loop
root.mainloop()
