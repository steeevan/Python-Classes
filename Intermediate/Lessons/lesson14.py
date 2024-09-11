import tkinter as tk  # Import the tkinter module for creating the GUI
from tkinter import filedialog, messagebox  # Import additional tkinter modules for file dialogs and message boxes

# Create a class called `TextEditor` to encapsulate the text editor's functionalities
class TextEditor:
    
    # __init__ is the constructor method for initializing the class
    def __init__(self, root):
        self.root = root  # Store the root window in an instance variable
        self.root.title("Text Editor")  # Set the title of the window
        self.root.geometry("800x600")  # Set the size of the window

        # Create a text area widget with undo functionality and word wrap
        self.text_area = tk.Text(self.root, undo=True, wrap="word")
        self.text_area.pack(expand=True, fill="both")  # Expand the text area to fill the window

        # Create a menu bar for the application
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)  # Set the menu bar for the root window

        # Create the File menu and add it to the menu bar
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        # Add commands to the File menu (New, Open, Save, Exit)
        self.file_menu.add_command(label="New")
        self.file_menu.add_command(label="Open")
        self.file_menu.add_command(label="Save")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)  # Add Exit command to close the application

        # Create the Edit menu and add it to the menu bar
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        # Add commands to the Edit menu (Undo, Redo, Cut, Copy, Paste)
        self.edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"))
        self.edit_menu.add_command(label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"))
        self.edit_menu.add_command(label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"))

# Entry point of the application
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    app = TextEditor(root)  # Instantiate the TextEditor class with the main window
    root.mainloop()  # Start the Tkinter event loop
