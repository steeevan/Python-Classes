import tkinter as tk
from tkinter import messagebox

def add_item():
    item = entry.get()
    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter an item.")

def remove_item():
    try:
        selected_item_index = listbox.curselection()[0]
        listbox.delete(selected_item_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select an item to remove.")

def clear_list():
    listbox.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Grocery List")

# Entry field
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Add button
add_button = tk.Button(root, text="Add Item", command=add_item)
add_button.pack(pady=5)

# Listbox to display items
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# Remove button
remove_button = tk.Button(root, text="Remove Selected Item", command=remove_item)
remove_button.pack(pady=5)

# Clear button
clear_button = tk.Button(root, text="Clear List", command=clear_list)
clear_button.pack(pady=5)

# Run the application
root.mainloop()
