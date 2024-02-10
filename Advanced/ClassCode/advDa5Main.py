from DiceImplementation import SixDice, TenDice,TwentyDice
from tkinter import messagebox
import tkinter as tk
import pygame


class DiceRollerApp:
    def __init__(self,master):
        # Created a variable 'Master' that will hold our tkinter screen
        self.master = master
        # Named our screen window
        master.title("Dice Roller")

        # Create a attribute tht holds a label 
        self.label = tk.Label(master, text="Select dice to roll")
        self.label.pack()

        # Create an attribute that holds a button
        self.six_sided_button = tk.Button(master,text="Roll 6-sided Dice", command= lambda: self.roll_dice(SixDice()))
        self.six_sided_button.pack()
        
        # Create an attribute that holds a button
        self.ten_sided_button = tk.Button(master,text="Roll 10-sided Dice", command= lambda: self.roll_dice(TenDice()))
        self.ten_sided_button.pack()


        # Create an attribute that holds a button
        self.twenty_sided_button = tk.Button(master,text="Roll 20-sided Dice", command= lambda: self.roll_dice(TwentyDice()))
        self.twenty_sided_button.pack()


        # Create a attrubute that holds our results
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        # Varibles that is a List type
        self.history = []

    def roll_dice(self,dice):
        result = dice.roll()
        self.result_label.config(text=f"Result: {result}")
        self.history.append(result)

def main():
    root = tk.Tk()
    app = DiceRollerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    
        

        


        
