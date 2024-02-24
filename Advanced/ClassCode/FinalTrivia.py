import tkinter as tk
from tkinter import messagebox
import random

class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def check_answer(self, selected_option):
        return selected_option == self.correct_answer

class GameRound:
    def __init__(self, questions):
        self.questions = questions
        self.current_question_index = 0
        self.score = 0

    def get_current_question(self):
        return self.questions[self.current_question_index]

    def check_answer(self, selected_option):
        current_question = self.get_current_question()
        if current_question.check_answer(selected_option):
            self.score += 1
        self.current_question_index += 1

    def is_round_over(self):
        return self.current_question_index >= len(self.questions)

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

class TriviaGameApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Trivia Game")
        self.master.geometry("500x300")

        self.current_round = None
        self.player = Player("Player 1")

        self.label_question = tk.Label(self.master, text="", wraplength=400, font=("Arial", 12))
        self.label_question.pack()

        self.radio_var = tk.IntVar()
        self.radio_buttons = []
        for i in range(4):
            radio_button = tk.Radiobutton(self.master, text="", variable=self.radio_var, value=i, font=("Arial", 10))
            radio_button.pack(anchor=tk.W)
            self.radio_buttons.append(radio_button)

        self.button_submit = tk.Button(self.master, text="Submit", command=self.submit_answer, font=("Arial", 12))
        self.button_submit.pack()

        self.load_random_round()

    def load_random_round(self):
        categories = [HistoryTrivia, ScienceTrivia]  # Add more categories as needed
        trivia_category = random.choice(categories)
        self.current_round = trivia_category()
        self.load_next_question()

    def load_next_question(self):
        if not self.current_round.is_round_over():
            question = self.current_round.get_current_question()
            self.label_question.config(text=question.question)
            for i, option in enumerate(question.options):
                self.radio_buttons[i].config(text=option)
            self.button_submit.config(state=tk.NORMAL)
        else:
            messagebox.showinfo("Game Over", f"Your final score: {self.player.score}")

    def submit_answer(self):
        selected_option = self.radio_var.get()
        if selected_option != -1:
            self.current_round.check_answer(selected_option)
            self.player.score = self.current_round.score
            self.load_next_question()
            self.radio_var.set(-1)  # Reset radio selection
        else:
            messagebox.showwarning("Warning", "Please select an option!")

class HistoryTrivia(GameRound):
    def __init__(self):
        questions = [
            Question("What year did World War I begin?", ["1914", "1915", "1916", "1917"], 0),
            Question("Who was the first President of the United States?", ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "John Adams"], 2),
            Question("Who wrote 'To Kill a Mockingbird'?", ["Harper Lee", "John Steinbeck", "Mark Twain", "J.K. Rowling"], 0),
        ]
        super().__init__(questions)

class ScienceTrivia(GameRound):
    def __init__(self):
        questions = [
            Question("What is the chemical symbol for water?", ["H2O", "CO2", "NaCl", "O2"], 0),
            Question("What planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter", "Saturn"], 1),
            Question("What is the powerhouse of the cell?", ["Nucleus", "Mitochondria", "Ribosome", "Endoplasmic Reticulum"], 1),
        ]
        super().__init__(questions)

def main():
    root = tk.Tk()
    app = TriviaGameApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
