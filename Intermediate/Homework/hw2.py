import tkinter as tk
from tkinter import messagebox as mb
#1
#listbox: a type of widget to display different items you can pick from
#StringVar: a command that takes in a variable as a string
#messagebox: something from tkinter that allows pop-up windows
#pack geometry manager: organizes widgets into rows/columns

#2
root=tk.Tk()
root.title('Text Updater')
root.geometry('250x250')

def update_label(text):
    text.get()
    if text!='':
        text.config
    else:
        mb.showwarning('You cannot type in nothing')

entry=tk.Entry(root, width=50)
entry.pack(pady=10)

label=tk.Label(root, width=50, text='Your text will appear here')
label.pack(pady=10)

button=tk.Button(root, text='add text', command=update_label(entry))
button.pack(pady=10)
































root.mainloop()
