import tkinter as tk  # Import the tkinter library for GUI development
from tkinter import messagebox, ttk  # Import additional tkinter components
import random  # Import the random module for generating random numbers

# Initialize a list to keep track of the rolls
rolls = []
# Create a variable to count the number of guesses
guess_counter = 0

# Function to roll the dice
def roll_dice():
    global guess_counter
    try:
        # Get the user's guess from the entry widget
        user_pick = int(entry.get())
        
        # Check if the guess is within the valid range
        if user_pick < 1 or user_pick > 6:
            messagebox.showerror("Invalid Input", "Please enter a number between 1 and 6")
            return

        # Reset labels and disable the roll button during animation
        result_label.config(text="")
        match_label.config(text="")
        roll_button.config(state=tk.DISABLED)
        memo_label.config(text="")

        # Animation loop to simulate rolling the dice
        for _ in range(10):
            rolled_number = random.randint(1, 6)  # Generate a random number between 1 and 6
            result_label.config(text=f"Rolling... {rolled_number}")
            root.update()  # Update the GUI
            root.after(100)  # Pause for 100ms for animation effect

        # Enable the roll button again
        roll_button.config(state=tk.NORMAL)
        rolled_number = random.randint(1, 6)  # Generate the final roll result
        result_label.config(text=f"You rolled a {rolled_number}")
        rolls.append(rolled_number)  # Add the roll result to the rolls list

        # Update the table with the roll results
        rolls_table.insert("", tk.END, values=(len(rolls), rolled_number))
        
        # Check if the rolled number matches the user's guess
        if rolled_number == user_pick:
            match_label.config(text="Congratulations! You guessed correctly!")
            guess_counter = 0
        else:
            match_label.config(text="Sorry, try again!")
            guess_counter += 1
            # Provide a funny memo after a certain number of guesses
            if guess_counter >= 15:
                memo_label.config(text="Here's a funny memo for you!")  # Placeholder text for memo
                guess_counter = 0

    # Handle invalid input
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number")

# F
