# Introduction to Tkinter module

import tkinter as tk  # Import the Tkinter library for GUI applications

def calculate():
    try:
        # Get numbers from the entry fields and convert them to floats
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        op = operation.get()  # Get the selected operation from the dropdown menu

        # Perform the selected operation
        if op == "+":
            result = add(num1, num2)  # Call the add function if "+" is selected
        elif op == "-":
            result = subtract(num1, num2)  # Call the subtract function if "-" is selected

        # Display the result in the result label
        update_result_label("Result: " + str(result))
        
    except ValueError:
        # Handle invalid input by updating the result label
        update_result_label("Invalid input")

def add(x, y):
    return x + y  # Return the sum of x and y

def subtract(x, y):
    return x - y  # Return the difference between x and y

def update_result_label(message):
    result_label.config(text=message)  # Update the text of the result label

def clear():
    # Clear the entry fields and reset the result label
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    update_result_label("Result:")

# Create a window for our calculator
root = tk.Tk()  # Initialize the main window
root.title("Enhanced Calculator")  # Set the title of the window

# Entry fields for numbers
entry_num1 = tk.Entry(root, width=10)  # Create an entry field for the first number
entry_num2 = tk.Entry(root, width=10)  # Create an entry field for the second number

# Place the entry fields in a grid layout
entry_num1.grid(row=0, column=0, padx=5, pady=5)
entry_num2.grid(row=0, column=2, padx=5, pady=5)

# Default selected operation
operation = tk.StringVar(root)  # Create a StringVar to store the selected operation
operation.set("+")  # Set the default operation to addition

# Dropdown menu for selecting the operation
operation_menu = tk.OptionMenu(root, operation, "+", "-")  # Create an option menu with "+" and "-" options
operation_menu.grid(row=0, column=1, padx=5, pady=5)  # Place the dropdown menu in the grid

# Button to calculate the result
calc_button = tk.Button(root, text="Calculate", command=calculate)  # Create a button that calls the calculate function
calc_button.grid(row=1, column=0, padx=5, pady=5)  # Place the button in the grid

# Button to clear the input fields and result
clear_button = tk.Button(root, text="Clear", command=clear)  # Create a button that calls the clear function
clear_button.grid(row=2, column=0, padx=5, pady=5)  # Place the button in the grid

# Label to display the result
result_label = tk.Label(root, text="Result:")  # Create a label to show the result
result_label.grid(row=3, columnspan=3, padx=5, pady=5)  # Place the label in the grid, spanning three columns

root.mainloop()  # Start the Tkinter event loop to display the window and handle user interactions
