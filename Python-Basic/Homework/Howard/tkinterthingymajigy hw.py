import tkinter as tk

root = tk.Tk()

root.title("USER INFORMATION")

label1 = tk.Label(root, text="hello, enter your name in the text box bellow")
label1.pack()

def on_entry_change(event):
    content = entry1.get()
    result_label.config(text=f"You entered: {content}")

def on_entry_change2(event):
    content = text1.get("1.0",tk.END)
    result_label2.config(text=f"You entered: {content}")

entry1 = tk.Entry(root,width=50)
entry1.bind("<KeyRelease>",on_entry_change)
entry1.pack()

result_label = tk.Label(root,text="")
result_label.pack()

label2 = tk.Label(root, text="PERSONAL NOTE")
label2.pack()
text1 = tk.Text(root,height = 5, width = 30)
text1.bind("<KeyRelease>",on_entry_change2)
text1.pack()

result_label2 = tk.Label(root,text="")
result_label2.pack()

        
var = tk.IntVar()

def on_checkbutton_click():
    if var.get():
        result_label3.config(text="subscribed")
    else:
        result_label3.config(text="unsubscribed")
    
checkbutton = tk.Checkbutton(root,text="subscribe to newsletter", variable = var, command = on_checkbutton_click)
checkbutton.pack()

result_label3 = tk.Label(root,text="")
result_label3.pack()

languages = [("CHINESE",1),("ENGLISH",2),("SPANISH",3)]

languages_var = tk.StringVar()
def on_radio_button_click():
    result_label4.config(text=f"Selected language: {languages_var.get()}")
for (language, value) in languages:
    radio = tk.Radiobutton(root,text=language,variable=languages_var,value = value,command = on_radio_button_click)
    radio.pack()
    
result_label4 = tk.Label(root,text="")
result_label4.pack()

frame = tk.Frame(root,width = 400, height = 600,bg = "lightblue")
frame.pack()

def on_button_click():
    result_label5.config(text="button was clicked")

button = tk.Button(frame,text = "click me", command = on_button_click)
button.pack(side='top')

result_label5 = tk.Label(frame,text="")
result_label5.pack(side='bottom')

root.mainloop() 
