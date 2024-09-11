import tkinter as tk  # Import the Tkinter library for creating GUI applications
from tkinter import messagebox  # Import the messagebox module for displaying alerts

# Create the main application window
root = tk.Tk()  # Initialize the main application window
root.title("To-Do List")  # Set the title of the window
root.geometry("500x400")  # Set the dimensions of the window

# Lists to store the tasks and their completion status
tasks = []  # List to store task descriptions
completed_status = []  # List to store completion status of tasks (True/False)

# Function to update the listbox with tasks and their status
def update_listbox():
    task_listbox.delete(0, tk.END)  # Clear the current contents of the listbox

    # Insert each task into the listbox with its number and status
    for index, task in enumerate(tasks):
        status = "(completed)" if completed_status[index] else "(uncompleted)"
        task_listbox.insert(tk.END, f"{index + 1}. {task} {status}")

    update_status_labels()  # Update the status labels showing completed and uncompleted tasks

# Function to update the status labels for completed and uncompleted tasks
def update_status_labels():
    completed_count = sum(completed_status)  # Count the number of completed tasks
    uncompleted_count = len(tasks) - completed_count  # Calculate the number of uncompleted tasks

    # Update the labels with the counts
    completed_label.config(text=f"Completed Tasks: {completed_count}")
    uncompleted_label.config(text=f"Uncompleted Tasks: {uncompleted_count}")

# Function to add a new task to the list
def add_task():
    task = task_entry.get()  # Get the text entered in the task entry field

    if task != "":  # Check if the task entry is not empty
        tasks.append(task)  # Add the new task to the tasks list
        completed_status.append(False)  # Initialize the completion status as False
        update_listbox()  # Update the listbox to reflect the new task
        task_entry.delete(0, tk.END)  # Clear the task entry field
    else:
        messagebox.showwarning("Warning", "You must enter a task.")  # Show a warning if the entry is empty

# Function to remove the selected task from the list
def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]  # Get the index of the selected task
        del tasks[selected_task_index]  # Remove the selected task from the tasks list
        del completed_status[selected_task_index]  # Remove the completion status of the selected task
        update_listbox()  # Update the listbox to reflect the changes
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to remove.")  # Show a warning if no task is selected

# Function to mark the selected task as completed
def mark_task_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]  # Get the index of the selected task
        completed_status[selected_task_index] = True  # Mark the task as completed
        update_listbox()  # Update the listbox to reflect the changes
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to mark as completed.")  # Show a warning if no task is selected

# Create the GUI components (Graphic User Interface)
# Entry widget to input tasks
task_entry = tk.Entry(root, width=40)  # Create an Entry widget for task input
task_entry.pack(pady=10)  # Add the Entry widget to the window with padding

# Button to add tasks
add_tasks_button = tk.Button(root, text="Add Task", command=add_task)  # Create a Button to add tasks
add_tasks_button.pack(pady=5)  # Add the Button to the window with padding

# Button to remove tasks
remove_tasks_button = tk.Button(root, text="Remove Task", command=remove_task)  # Create a Button to remove tasks
remove_tasks_button.pack(pady=5)  # Add the Button to the window with padding

# Button to mark tasks as completed
mark_tasks_button = tk.Button(root, text="Mark Task as Completed", command=mark_task_completed)  # Create a Button to mark tasks as completed
mark_tasks_button.pack(pady=5)  # Add the Button to the window with padding

# Listbox to display the tasks
task_listbox = tk.Listbox(root, width=50, height=15)  # Create a Listbox widget to show tasks
task_listbox.pack(pady=10)  # Add the Listbox to the window with padding

# Labels to display the number of completed and uncompleted tasks
completed_label = tk.Label(root, text="Completed Tasks: 0")  # Create a Label to show completed tasks count
completed_label.pack()  # Add the Label to the window

# Label to display the number of uncompleted tasks
uncompleted_label = tk.Label(root, text="Uncompleted Tasks: 0")  # Create a Label to show uncompleted tasks count
uncompleted_label.pack()  # Add the Label to the window

# Start the main event loop
root.mainloop()  # Run the Tkinter event loop to display the window and handle user interactions
