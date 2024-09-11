from tkinter import *  # Import all widgets from tkinter
from tkinter.ttk import *  # Import the Combobox widget from tkinter.ttk
from datetime import datetime, timedelta  # Import datetime and timedelta for time calculations

# Create the main Tkinter window
root = Tk()
root.title("Clock")  # Set the title of the window

# Create a dictionary to map time zones to their UTC offsets
time_zone = {
    "PST": -7,  # Pacific Standard Time
    "EST": -3,  # Eastern Standard Time
    "UTC": 0,   # Coordinated Universal Time
    "JST": 10,  # Japan Standard Time
}

# Function to update the time displayed on the label based on the selected time zone
def update_time():
    selected_timezone = time_zone[combo.get()]  # Get the UTC offset for the selected time zone
    utc_now = datetime.utcnow()  # Get the current UTC time
    selected_time = utc_now + timedelta(hours=selected_timezone)  # Adjust time based on the selected time zone
    current_time = selected_time.strftime("%H:%M:%S %p")  # Format the time as hours:minutes:seconds AM/PM

    time_label.config(text=f'{combo.get()}: {current_time}')  # Update the label with the current time
    time_label.after(1000, update_time)  # Call this function again after 1000 milliseconds (1 second)

# Function to toggle the visibility of the clock
def toggle_clock():
    if time_label.winfo_ismapped():  # Check if the time label is currently visible
        time_label.pack_forget()  # Hide the label
    else:
        time_label.pack(anchor="center")  # Show the label, centered
        update_time()  # Start updating the time

# Dropdown menu for selecting the time zone
combo = Combobox(root, value=list(time_zone.keys()))  # Create a combobox with time zone options
combo.current(0)  # Set the default selection to the first time zone
combo.bind("<<ComboboxSelected>>", lambda event: update_time())  # Update time when a new time zone is selected
combo.pack(pady=10)  # Add some vertical padding around the combobox

# Button to toggle the visibility of the clock
toggle_button = Button(root, text="Show/Hide", command=toggle_clock)  # Create a button to show/hide the clock
toggle_button.pack(pady=10)  # Add some vertical padding around the button

# Label to display the time
time_label = Label(root, font=('calibri', 23, 'bold'),  # Set the font and style of the label
                   background='yellow', foreground='pink')  # Set background and foreground colors
time_label.pack(anchor="center")  # Initially display the label, centered

# Update the time every second
update_time()

# Start the Tkinter event loop
root.mainloop()
