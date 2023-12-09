import tkinter as tk

#Window/Title
root = tk.Tk()

root.title("Exercises today")


#Define Function to bind the entry key
def on_entry_change(event):
    content = entry1.get()
    result_label.config(text=f"You entered:{content}")
def on_text_entry(event):
    content = text1.get("1.0",tk.END)
    result_label2.config(text=f"You entered:{content}")

result_label = tk.Label(root,text="")
result_label.pack()

#Entry Widget
entry1 = tk.Entry(root, width=30)
entry1.bind("<KeyRelease>", on_entry_change)
entry1.pack()


#Text Widget
text1 = tk.Text(root, height=5, width=30)
text1.bind("<KeyRelease>", on_text_entry)
text1.pack()

result_label2 = tk.Label(root,text="")
result_label2.pack()

#CheckButtonWidget
checkbutton = tk.Checkbutton(root,text="Check me!")
checkbutton.pack()

#RadioButtonWidget
fruits = [("APPLE","apple"),("BANANA","banana"),("ORANGE","orange")]

fruit_var = tk.StringVar()
def on_radiobutton_click():
    result_label3.configure(text=f"Selected Fruit: {fruit_var.get()}")
for fruit, value in fruits:
    radio = tk.Radiobutton(root, text=fruit, variable=fruit_var,value=value,command=on_radiobutton_click)
    radio.pack()

result_label3=tk.Label(root,text="")
result_label3.pack()

def on_button_click():
    result_label4.config(text="button was clicked")
frame = tk.Frame(root, width = 200, height=300, bg = "lightblue")
frame.pack()
button = tk.Button(frame, text="Click me", command = on_button_click)
button.pack()

result_label4 = tk.Label(frame, text="")
result_label4.pack() 


















root.mainloop()

