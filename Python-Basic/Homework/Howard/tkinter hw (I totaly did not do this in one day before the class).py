import tkinter as tk
import random

names = ["ZACH","EDDIE","JESSICA","KYLE","GAMER_BOY_89756"]
message = ["HEJJO THERE!!!","HOWDY PARTNER!!!","🤪","😄","URGGG FLARPPP!!!"]
bg_color = ["blue","red","yellow","green","orange"]
num = 0


root = tk.Tk()

root.title("IMFORMATION DISPLAY")
root.geometry("400x200")



label1 = tk.Label(root, text="hello, this is HOWARD")
label2 = tk.Label(root, text="WELCOME!!!HELLO!!!")
label3 = tk.Label(root, text=str(num))



label1.pack()
label2.pack()
label3.pack()


def button_function1():
    label1.config(text="hello, this is "+names[random.randint(0,4)])
    label2.config(text=message[random.randint(0,4)])
    label1.update_idletasks()
    label2.update_idletasks()

def button_function2():
    root.config(background=bg_color[random.randint(0,4)])

def button_function3():
    global num
    num = num + 1
    label3.config(text=str(num))

    

button1 = tk.Button(root,text="SHOW INFO", command = button_function1)
button1.pack()
button2 = tk.Button(root,text="CHANGE COLOR", command = button_function2)
button2.pack()
button3 = tk.Button(root,text="CHANGE NUMBER", command = button_function3)
button3.pack()

root.mainloop()
