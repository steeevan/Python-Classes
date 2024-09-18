import tkinter as tk  # Import the tkinter module for GUI
from tkinter import messagebox  # Import messagebox for showing warning dialogs

# Function to add an item to the listbox
def add_item():
    item = entry.get()  # Get the text from the entry widget
    if item:  # Check if the entry is not empty
        listbox.insert(tk.END, item)  # Add the item to the end of the listbox
        entry.delete(0, tk.END)  # Clear the entry widget after adding the item
    else:  # If the entry is empty
        messagebox.showwarning("Warning", "Please enter an item.")  # Show a warning dialog

# Function to remove the selected item from the listbox
def remove_item():
    try:
        selected_item_index = listbox.curselection()[0]  # Get the index of the selected item
        listbox.delete(selected_item_index)  # Remove the item at the selected index
    except IndexError:  # If no item is selected (empty selection)
        messagebox.showwarning("Warning", "Please select an item to remove.")  # Show a warning dialog

# Function to clear all items from the listbox
def clear_list():
    listbox.delete(0, tk.END)  # Delete all items in the listbox

# Create the main window of the application
root = tk.Tk()
root.title("Grocery List")  # Set the title of the window

# Create an entry widget for user input
entry = tk.Entry(root, width=50)  # Create an entry field with a width of 50 characters
entry.pack(pady=10)  # Add the entry widget to the window and add vertical padding

# Create an "Add Item" button
add_button = tk.Button(root, text="Add Item", command=add_item)  # Button to add items, linked to the add_item function
add_button.pack(pady=5)  # Add the button to the window and add vertical padding

# Create a listbox to display the items
listbox = tk.Listbox(root, width=50, height=10)  # Create a listbox with a width of 50 characters and height of 10 items
listbox.pack(pady=10)  # Add the listbox to the window and add vertical padding

# Create a "Remove Selected Item" button
remove_button = tk.Button(root, text="Remove Selected Item", command=remove_item)  # Button to remove selected items, linked to the remove_item function
remove_button.pack(pady=5)  # Add the button to the window and add vertical padding

# Create a "Clear List" button
clear_button = tk.Button(root, text="Clear List", command=clear_list)  # Button to clear all items, linked to the clear_list function
clear_button.pack(pady=5)  # Add the button to the window and add vertical padding

# Start the Tkinter event loop
root.mainloop()  # Run the application
