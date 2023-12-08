import tkinter as tk

root = tk.Tk

root.title("User Info")

#1
def entry1_change(event):
    content = entry1.get()
    result_label.config(text=f"Your name is:{content}")
def entry2_change(event):
    content = text1.get("1.0",tk.END)
    result_label2.config(text=f"You entered:{content}")

result_label = tk.Label(root,text="")
result_label.pack()

entry1 = tk.Entry(root, width=30)
entry1.bind("<KeyRelease>", entry1_change)
entry1.pack()


text1 = tk.Text(root, height=5, width=30)
text1.bind("<KeyRelease>", entry1_change)
text1.pack()

result_label2 = tk.Label(root,text="")
result_label2.pack()

#2
entry2 = tk.title("Personal note")
entry2 = tk.Entry(root, width=30)
entry2.bind("<KeyRelease>", on_entry_change)
entry2.pack()
text2 = tk.Text(root, height=5, width=30)
text2.bind("<KeyRelease>", entry1_change)
text2.pack()
result_label3 = tk.Label(root,text="")
result_label3.pack()


#3
checkbutton = tk.Checkbutton(root,text="Subscribe to newsletter!")
checkbutton.pack()

#4
languages = [("ENGLISH","english"),("SPANISH","spanish"),("CHINESE","chinese")]
lang_var = tk.StringVar()
def on_radiobutton_click():
    result_label4.configure(text=f"Selected Language: {lang_var.get()}")
for language, value in fruits:
    radio = tk.Radiobutton(root, text=language, variable=lang_var,value=value,command=on_radiobutton_click)
    radio.pack()

result_label4=tk.Label(root,text="")
result_label4.pack()

#5
def on_button_click():
    result_label5.config(text="Yay you clicked the button!!!")
frame = tk.Frame(root, width = 200, height=300, bg = "lightblue")
frame.pack()
button = tk.Button(frame, text="Click me", command = on_button_click)
button.pack()

result_label4 = tk.Label(frame, text="")
result_label4.pack() 








root.mainloop
