import tkinter as tk
import string
import random
from tkinter import messagebox


class PasswordGenerator:
    def __init__(self,chickenSoul):
        self.root = chickenSoul
        self.root.title("Password Generator")
        self.root.geometry("400x300")


        # Label for password length
        self.label = tk.Label(self.root, text="Enter password Length: ")
        self.label.pack(pady=10)

        # Entry widget to input password length
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=5)


        # variable to hold teh generate password
        self.password_var = tk.StringVar()


        # Label to display the generated password
        self.password_label = tk.Label(self.root, textvariable=self.password_var, font=("Arial", 12))
        self.password_label.pack(pady=10)

        # Button to copy te password to clipboard
        self.copy_button = tk.Button(self.root, text="Copy to Clipboard",command=self.copy_password)
        self.copy_button.pack(pady=10)

        # Button for our Generate Password
        # generate_password()
        self.generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.entry.get())
            if length <= 0:
                raise ValueError("Password Length must be positive! You noob!")
            characters = string.aschi_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            self.password.set(password)
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number for the password!")

    def copy_password(self):
        password = self.password_var.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Copied","Password copied to clipboard")
        else:
            messagebox.showwarning("No password", "Please generate a password first you baloney")


# Create an instance of your class, and run you project
# Wirte additional code if needed to help run your class
# hint: you need a main window to run the app




    
            
        
        
        
