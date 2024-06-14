import tkinter as tk
from tkinter import messagebox, ttk
import random

# Initialize list to keep track of rolls
rolls = []
guess_counter = 0  # Counter to track the number of guesses

# Function to roll the dice
def roll_dice():
    global guess_counter
    try:
        user_pick = int(entry.get())
        if user_pick < 1 or user_pick > 6:
            messagebox.showerror("Invalid Input", "Please enter a number between 1 and 6")
            return

        result_label.config(text="")
        match_label.config(text="")
        roll_button.config(state=tk.DISABLED)
        meme_label.config(text="")  # Clear the meme label

        # Animation loop
        for _ in range(10):  
            rolled_number = random.randint(1, 6)
            result_label.config(text=f"Rolling... {rolled_number}")
            root.update()
            root.after(100)  # Pause for 100ms for animation effect

        roll_button.config(state=tk.NORMAL)
        rolled_number = random.randint(1, 6)
        result_label.config(text=f"You rolled a {rolled_number}")
        rolls.append(rolled_number)

        # Update table
        rolls_table.insert("", tk.END, values=(len(rolls), rolled_number))
        if rolled_number == user_pick:
            match_label.config(text="Congratulations! You guessed correctly!")
            guess_counter = 0  # Reset counter
        else:
            match_label.config(text="Sorry, try again!")
            guess_counter += 1
            if guess_counter >= 15:
                meme_label.config(text="Here's a funny meme for you!")  # Placeholder text for meme
                guess_counter = 0  # Reset counter

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number")

# Function to clear the data
def clear_data():
    global rolls, guess_counter
    rolls = []
    guess_counter = 0
    for item in rolls_table.get_children():
        rolls_table.delete(item)
    result_label.config(text="")
    match_label.config(text="")
    meme_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Dice Roll Game")

# Create and place the widgets
tk.Label(root, text="Pick a number (1-6):").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

roll_button = tk.Button(root, text="Roll Dice", command=roll_dice)
roll_button.pack(pady=10)

clear_button = tk.Button(root, text="Clear Data", command=clear_data)
clear_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

match_label = tk.Label(root, text="")
match_label.pack(pady=5)

meme_label = tk.Label(root, text="", fg="red")  # Label for meme or funny message
meme_label.pack(pady=10)

# Create table for roll history
columns = ("Attempt", "Rolled Number")
rolls_table = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    rolls_table.heading(col, text=col)
rolls_table.pack(pady=10)

# Start the main event loop
root.mainloop()
