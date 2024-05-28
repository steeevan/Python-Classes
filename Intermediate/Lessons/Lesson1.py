'''
*Introduction to Tkinter module*
'''
import tkinter as tk
import math

def calculate():
    # perform the caluclation based on user input
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        op = operation.get()
        # + , - . *, / , √
        if op == "+":
            result = add(num1,num2)
        elif op == "-":
            result = subtract(num1,num2)
        elif op == "*":
            result = multiply(num1,num2)
        elif op == "/":
            result = divide(num1,num2)
        elif op =="√":
            result = square_root(num1)
        # Display update
        update_result_label("Result: " + str(result))
        
    except ValueError:
        #handle the invalid input
        update_result_label("Invalid Input")

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def square_root(x):
    return math.sqrt(x)

def clear():
    """Clear the input fields and result label."""
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    update_result_label("Result:")

def update_result_label(text):
    """Update the result label with the given text."""
    result_label.config(text=text)


    
# create a main window
root = tk.Tk()
root.title("Enhanced Calculator")

# Entry fileds for numbers
entry_num1 = tk.Entry(root,width=10)
entry_num1.grid(row = 0, column = 0, padx = 5, pady = 5)

operation = tk.StringVar(root)
operation.set("+")

#Dropdown for selecting operations
operation_menu = tk.OptionMenu(root,operation,"+","-")
operation_menu.grid(row=0,column=1,padx=5,pady=5)

entry_num2 = tk.Entry(root,width=10)
entry_num2.grid(row=0,column=2,padx=5,pady=5)

# Button to calculate
calc_button = tk.Button(root,text="Calculate",command=calculate)
calc_button.grid(row=1,column=0,padx=5,pady=5)
# -
# Button to clear
clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.grid(row=2, column=0, padx=5, pady=5)

# Label to display result
result_label = tk.Label(root, text="Result:")
result_label.grid(row=3, columnspan=3, padx=5, pady=5)

# Label to display history
history_label = tk.Label(root, text="", justify="left")
history_label.grid(row=4, columnspan=3, padx=5, pady=5)

root.mainloop()


