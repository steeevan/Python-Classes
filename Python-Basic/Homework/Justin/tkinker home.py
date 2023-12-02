import tkinter as tk
import random

cc = 0

def Quit():
    exit()


def Toggle:
    
    

def counter():
    cc += 1
    print(cc)
       
    

def pick_color():
    colors = ["red", "blue", "yellow", "green", "orange", "yellow", "cyan", "purple", "pink", "magenta"]
    pickedcolor = colors[random.randint(0,len(colors))]
    root.configure(bg=pickedcolor)


root = tk.Tk()
root.title("information display")
Information = tk.Label(root,text="Hi Justin")
color = tk.Button(root,text="color", command=pick_color)
Counter = tk.Button(root,text="counter", command=counter)
toggle = tk.Button(root,text="counter", command=Toggle)
qUit = tk.Button(root,text="quit", command=Quit)

Information.pack()
color.pack()
Counter.pack()
qUit.pack()
root.mainloop
