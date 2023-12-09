'''
# create function named SUM
# WIth two parameters, and returns the sum of the two parameters
def SUM(X,Y):
    return X + Y


z = SUM(15,15)
print(z)
'''
#------------------------------------------------------------------------
import tkinter as tk

def create_widgets():
    # Entry Widget to display the input and results
    entry_frame = tk.Frame(root)
    entry_frame.pack(pady=10)

    entry = tk.Entry(entry_frame,textvariable = result_var, font=('Arial', 18), bd = 10, insertwidth=4,width=14,justify = 'right')
    entry.grid(row=0,column=0,columnspan=4)

    #Buttons
    button_frame = tk.Frame(root)
    button_frame.pack()

    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+'
        ]

    row_val, col_val = 1, 0

    for button in buttons:
        tk.Button(button_frame, text=button, padx=20, pady=20, font = ("Arial",14), command= lambda b=button: on_button_click(b)).grid(row=row_val, column=col_val)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1
#------------------------------------------------------------------------------------------------------------

def on_button_click(button):

    current_text = result_var.get()

    if button == '=':
        try:
            result = eval(current_text)
            result_var.set(result)
        except Exception as e:
            result_var.set("Error")
    elif button == 'C':
        result_var.set('')
    else:
        result_var.set(current_text + button)
        




if __name__ == "__main__":
    root =tk.Tk()
    root.title("calculator")
    result_var = tk.StringVar()
    create_widgets()

    root.mainloop()


    
