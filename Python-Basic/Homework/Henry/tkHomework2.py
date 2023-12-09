import tkinter as tk
# ^- Importing tkinter but labeling as "tk"

root = tk.Tk()
# ^- Setting root for the main frame

root.title("User Information")
# ^- Setting a name for the window
#-------------------------------------------

# CUSTOM FUNCTIONS
def Subscription():
     if subscribe_var.get():
          # If user clicks the checkbutton. changes the text green and says subscribed
          SubscribeLabel.config(text="Subscribed",foreground="green")
     else:
          # If user clicks the checkbutton. changes the text red and says not subscribed
          SubscribeLabel.config(text="Not subscribed",foreground="red")
     
def NameInput_to_LabelUpdater (event):
     
     content = NameInput.get() # gets the content from the NameInput (Entry)
     
     NameLabel.config(text=f"{content}") # Configures the text to the content from the NameInput (Entry)

def TextInput_to_TextUpdater (event):
     
     content = TextInput.get() # gets the content from the TextInput (Entry)
     TextLabel.config(text=f"You typed: {content}") # Configures the text to the content from the TextInput (Entry)

# LABELS & WIDGETS
NameInput = tk.Entry(root,width=50)

TextLabel = tk.Label(root,text="")

TextInput = tk.Entry(root,width=50)

SubscribeLabel = tk.Label(root,text="Not subscribed",foreground="red")

#-------------------------------------------
subscribe_var = tk.BooleanVar()
subscribe_checkbox = tk.Checkbutton(root, text="Subscribe", variable=subscribe_var,command=Subscription)
# ^- Setting radiobutton (checkmark button) / VARS
#-------------------------------------------

# LANGUAGE WIDGETS


languages = {
      "English":  {"Hello":"Hello", "red":"red", "Computer": "Computer", "Goodbye": "Goodbye"},
      "French": {"Hello": "Bonjour", "red":"rouge", "Computer":"ordinateur", "Goodbye":"au revoir"},
      "Russian": {"Hello":"Привет", "red": "красный", "Computer":"компьютер", "Goodbye":"до свидания"}
}
# ^- Our dictionary with 3 languages, each with 4 labels to change
# CUSTOM FUNCTIONS | LANGUAGES
def ChangeLangauge(*args):  # Changes languages and gets StringVar
     DefaultLanguage = languagesVar.get()
     updateLanguage(DefaultLanguage)

def updateLanguage(current_language): # Updates languages (configs labels)
     Hello_Text = languages[current_language]["Hello"]
     Red_text = languages[current_language]["red"]
     Computer_text = languages[current_language]["Computer"]
     Goodbye_text = languages[current_language]["Goodbye"]

     HelloLabel.config(text=Hello_Text)
     RedLabel.config(text=Red_text)
     ComputerLabel.config(text=Computer_text)
     HelloLabel.config(text=Hello_Text)
     GoodbyeLabel.config(text=Goodbye_text)


HelloLabel = tk.Label(root,text="")
RedLabel = tk.Label(root,text="")
ComputerLabel = tk.Label(root,text="")
GoodbyeLabel = tk.Label(root,text="")
# ^- All labels (empty)
DefaultLanguage = tk.StringVar(value="English") # Default label language is English
languageLabel = tk.Label(root,text="") # First displaus english langauge on play

languagesVar = tk.StringVar(value=DefaultLanguage)
languagesVar.trace_add("write", ChangeLangauge) 
languageMenu = tk.OptionMenu(root,languagesVar,*languages.keys()) # Access our language dictionary with key

updateLanguage(DefaultLanguage.get())

     
#-------------------------------------------
NameLabel = tk.Label(root,text="")
# ^- Setting a label which we will update the name into the label




# BINDS
NameInput.bind("<KeyRelease>", NameInput_to_LabelUpdater)
TextInput.bind("<KeyRelease>", TextInput_to_TextUpdater)
# PACKS
NameLabel.pack()
NameInput.pack()
TextLabel.pack()
TextInput.pack()
SubscribeLabel.pack()
subscribe_checkbox.pack()
languageMenu.pack()
languageLabel.pack()
HelloLabel.pack()
RedLabel.pack()
ComputerLabel.pack()
GoodbyeLabel.pack()




root.mainloop()
# ^- Important step for the frame and UI assets to work