import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Lists to store tasks and their completion status
tasks = []
completed_status = []

# Function to update the listbox
def update_listbox():
    # Clear the current listbox
    task_listbox.delete(0, tk.END)
    # Insert each task into the listbox with its number and status
    for index, task in enumerate(tasks):
        status = "(completed)" if completed_status[index] else "(uncompleted)"
        task_listbox.insert(tk.END, f"{index + 1}. {task} {status}")
    update_status_labels()

# Function to update the status labels
def update_status_labels():
    completed_count = sum(completed_status)
    uncompleted_count = len(tasks) - completed_count
    completed_label.config(text=f"Completed Tasks: {completed_count}")
    uncompleted_label.config(text=f"Uncompleted Tasks: {uncompleted_count}")

# Function to add a task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        completed_status.append(False)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to remove a task
def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        del tasks[selected_task_index]
        del completed_status[selected_task_index]
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to remove.")

# Function to mark a task as completed
def mark_task_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]
        completed_status[selected_task_index] = True
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to mark as completed.")

# Create the GUI components
# Entry widget to input tasks
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Button to add tasks
add_task_button = tk.Button(root, text="Add Task", command=add_task)
add_task_button.pack(pady=5)

# Button to remove tasks
remove_task_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_task_button.pack(pady=5)

# Button to mark tasks as completed
mark_task_button = tk.Button(root, text="Mark Task as Completed", command=mark_task_completed)
mark_task_button.pack(pady=5)

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

# Labels to display the number of completed and uncompleted tasks
completed_label = tk.Label(root, text="Completed Tasks: 0")
completed_label.pack()

uncompleted_label = tk.Label(root, text="Uncompleted Tasks: 0")
uncompleted_label.pack()

# Start the main event loop
root.mainloop()
