import tkinter as tk
import random
root = tk.Tk()

root.title("Information Display")
def WelcomeMessage():
    print("Welcome Harry")
def PickColor():
    colors = ["Red", "blue", "Green"]
    PickColor = colors[random.randint(0,len(colors)-1)]
    root.configure(bg=PickColor)
def UpdateCount():
    
    NumberCounted = 0

is_toggled = tk.BooleanVar()
is_toggled.set(False)
def Toggle_text():
    if is_toggled.get():
        TextToggle.config(text="Text Off")
    else:
        TextToggle.config(text="Text On")
    is_toggled.set(not is_toggled.get())
def Closer():
    root.destroy()

exitbutton = tk.Button(root,text="close",command=Closer)
Label = tk.Label(root,text="Harry")
button = tk.Button(root, text="Show info",command=WelcomeMessage)
buttonColorChanger = tk.Button(root, text="Change window to random color",command=PickColor)
TextToggle = tk.Button(root,text="toggle text",command=Toggle_text)

exitbutton.pack()
Label.pack()
button.pack()
buttonColorChanger.pack()
TextToggle.pack()
root.mainloop()