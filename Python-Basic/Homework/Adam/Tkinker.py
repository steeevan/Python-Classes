import tkinter as tk

#1
def update_info():
    greeting(text="Welcome to Information Display!")
    name(text="My name is Adam")

window = tk.Tk()
window.title("Information Display")

greeting = tk.Label(window, text="Welcome to Tkinter!"))
greeting.pack()


name = tk.Label(window, text="My name is unknown"))
name.pack()

info_button = tk.Button(window, text="Show info", command=update_info)
info_button.pack()

window.mainloop()

#2
change_color = tk.Button(window, text ="change color!", command=pick_color)
red_bg = tk.Button(root, text="change color!", command=red)
blue_bg = tk.Button(root, text="change color!", command=blue)
green_bg = tk.Button(root, text="change color!", command=green)

#3
def counter():
    print("I was clicked")
def counter2():
    print("Button 2 was clicked!") 
def counter3():
    print("Button 3 was clicked!")

#4
    HELP

#5
exit_button = tk.Button(windwo, text = "EXIT", command=exit)




window.mainloop()



