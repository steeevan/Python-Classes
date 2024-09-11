import tkinter as tk  # Import the tkinter module for GUI
from tkinter import messagebox  # Import messagebox for showing alerts

# List to store contacts
contacts = []

# Function to save contact information to the list
def save_contact():
    name = entry_name.get()  # Retrieve the name from the entry field
    phone = entry_phone.get()  # Retrieve the phone number from the entry field
    email = entry_email.get()  # Retrieve the email from the entry field

    # Check if any field is empty
    if name == "" or phone == "" or email == "":
        messagebox.showwarning("Input Error", "All fields are required.")  # Show warning if fields are missing
    else:
        # Create a dictionary with the contact information and append it to the contacts list
        contact_info = {'Name': name, 'Phone': phone, 'Email': email}
        contacts.append(contact_info)
        messagebox.showinfo("Success", "Contact saved successfully!")  # Show success message
        # Clear the entry fields
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)

# Function to display contacts in a new window
def display_contacts():
    contacts_window = tk.Toplevel()  # Create a new top-level window
    contacts_window.title("Contacts List")  # Set the title of the new window
    
    # Display each contact in the new window
    for idx, contact in enumerate(contacts, start=1):
        contact_label = tk.Label(contacts_window, text=f"{idx}. Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}")
        contact_label.pack()  # Pack each label into the new window

# Create the main window
root = tk.Tk()
root.title("Contact Manager")  # Set the title of the main window

# Create input fields for Name, Phone, and Email
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=10)  # Position the name label

entry_name = tk.Entry(root)  # Create an entry field for the name
entry_name.grid(row=0, column=1, padx=10, pady=10)  # Position the name entry field

label_phone = tk.Label(root, text="Phone:")
label_phone.grid(row=1, column=0, padx=10, pady=10)  # Position the phone label

entry_phone = tk.Entry(root)  # Create an entry field for the phone number
entry_phone.grid(row=1, column=1, padx=10, pady=10)  # Position the phone entry field

label_email = tk.Label(root, text="Email:")
label_email.grid(row=2, column=0, padx=10, pady=10)  # Position the email label

entry_email = tk.Entry(root)  # Create an entry field for the email
entry_email.grid(row=2, column=1, padx=10, pady=10)  # Position the email entry field

# Create buttons to save contact and display contacts
btn_save = tk.Button(root, text="Save Contact", command=save_contact)  # Button to save contact
btn_save.grid(row=3, column=0, columnspan=2, pady=10)  # Position the save button

btn_display = tk.Button(root, text="Display Contacts", command=display_contacts)  # Button to display contacts
btn_display.grid(row=4, column=0, columnspan=2, pady=10)  # Position the display button

# Start the Tkinter main loop
root.mainloop()
