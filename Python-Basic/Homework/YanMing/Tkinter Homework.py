import tkinter as tk
import random
root = tk.Tk()
def close():
   root.destroy()
   root.quit()
def Toggle_Text():
    label1["text"] = ""
    label2["text"] = ""
def show_info():
    label1["text"] = "Welcome to this window"
    label2["text"] = "Yanming"
def counter():
    label["text"] += 1
def change_color():
    colors = ["blue","red","green","purple","pink"]
    root.configure(bg=random.choice(colors))
root.title("Information Display")
btn = tk.Button(root, text = "Change color",command = change_color)

btn2 = tk.Button(root, text= "Show Info",command = show_info)

btn3 = tk.Button(root, text= "Toggle Text.",command = Toggle_Text)
                 
label1 = tk.Label(root, text = "")
                 
label2 = tk.Label(root, text = "")

btn4 = tk.Button(root, text = "Exit Program.", command = close)
                 
label = tk.Label(root, text = 0)
                 
btn1 = tk.Button(root, text = "Increment Counter", command = counter)

btn2.pack()

label1.pack()

label2.pack()
                 
btn3.pack()
                 
btn.pack()
                 
btn1.pack()              
                 
label.pack()

btn4.pack()
                 
root.mainloop()
