import tkinter as tk  # Import the tkinter library for GUI development

# Create the main application window
root = tk.Tk()  # Initialize the main window
root.title("Basic Login System")  # Set the title of the window
root.geometry("550x250")  # Set the dimensions of the window

# Function to update the result on the screen
def update_result_on_screen():
    un = username_entry.get()  # Get the text from the username entry field
    pw = password_entry.get()  # Get the text from the password entry field
    info = "Username: " + str(un) + " | Password: " + str(pw)  # Create a string with the username and password

    result_label.config(text=str(info))  # Update the result_label with the created string

# Label for username
username_label = tk.Label(root, text="Username:")  # Create a label for the username
username_label.pack(pady=5)  # Add the label to the window with padding

# Label for password
password_label = tk.Label(root, text="Password:")  # Create a label for the password
password_label.pack(pady=5)  # Add the label to the window with padding

# Label for result
result_label = tk.Label(root, text="")  # Create a label to display the result
result_label.pack(pady=10)  # Add the label to the window with padding

# Username entry
username_entry = tk.Entry(root)  # Create an entry widget for username input
username_entry.pack(pady=5)  # Add the entry widget to the window with padding

# Password entry
password_entry = tk.Entry(root, show='*')  # Create an entry widget for password input with masked characters
password_entry.pack(pady=5)  # Add the entry widget to the window with padding

# Button for submit
submit_button = tk.Button(root, text="Submit", command=update_result_on_screen)  # Create a button that triggers the update_result_on_screen function
submit_button.pack(pady=10)  # Add the button to the window with padding

# Start the main event loop
root.mainloop()  # Display the window and start handling user events
