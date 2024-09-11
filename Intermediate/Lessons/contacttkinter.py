import tkinter as tk
from tkinter import messagebox

# List to store contacts
contacts = []

# Function to save contact information to a list
def save_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()

    if name == "" or phone == "" or email == "":
        messagebox.showwarning("Input Error", "All fields are required.")
    else:
        contact_info = {'Name': name, 'Phone': phone, 'Email': email}
        contacts.append(contact_info)
        messagebox.showinfo("Success", "Contact saved successfully!")
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)

# Function to display contacts
def display_contacts():
    contacts_window = tk.Toplevel()
    contacts_window.title("Contacts List")
    
    for idx, contact in enumerate(contacts, start=1):
        contact_label = tk.Label(contacts_window, text=f"{idx}. Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}")
        contact_label.pack()

# Create the main window
root = tk.Tk()
root.title("Contact Manager")

# Create input fields for Name, Phone, and Email
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=10)

entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

label_phone = tk.Label(root, text="Phone:")
label_phone.grid(row=1, column=0, padx=10, pady=10)

entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1, padx=10, pady=10)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=2, column=0, padx=10, pady=10)

entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=10, pady=10)

# Create buttons to save contact and display contacts
btn_save = tk.Button(root, text="Save Contact", command=save_contact)
btn_save.grid(row=3, column=0, columnspan=2, pady=10)

btn_display = tk.Button(root, text="Display Contacts", command=display_contacts)
btn_display.grid(row=4, column=0, columnspan=2, pady=10)

# Start the Tkinter main loop
root.mainloop()
