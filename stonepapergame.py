import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        self.root.geometry("400x400")
        self.root.configure(bg="purple")  

        self.user_score = 0
        self.computer_score = 0

        self.user_choice_label = tk.Label(root, text="Your Choice:", font=("Helvetica", 14), bg="purple", fg="white")
        self.user_choice_label.pack(pady=10)

        self.choices_frame = tk.Frame(root, bg="purple")
        self.choices_frame.pack()

        self.rock_button = tk.Button(self.choices_frame, text="Rock", command=lambda: self.play_game("Rock"))
        self.rock_button.grid(row=0, column=0, padx=10)

        self.paper_button = tk.Button(self.choices_frame, text="Paper", command=lambda: self.play_game("Paper"))
        self.paper_button.grid(row=0, column=1, padx=10)

        self.scissors_button = tk.Button(self.choices_frame, text="Scissors", command=lambda: self.play_game("Scissors"))
        self.scissors_button.grid(row=0, column=2, padx=10)

        self.result_frame = tk.Frame(root, bg="purple")
        self.result_frame.pack(pady=20)

        self.user_result_label = tk.Label(self.result_frame, text="", font=("Helvetica", 14), bg="purple", fg="white")
        self.user_result_label.grid(row=0, column=0, padx=10)

        self.computer_result_label = tk.Label(self.result_frame, text="", font=("Helvetica", 14), bg="purple", fg="white")
        self.computer_result_label.grid(row=0, column=1, padx=10)

        self.score_label = tk.Label(root, text=f"Score: You {self.user_score} - {self.computer_score} Computer", font=("Helvetica", 12), bg="purple", fg="white")
        self.score_label.pack()

        self.play_again_button = tk.Button(root, text="Play Again", command=self.reset_game)
        self.play_again_button.pack(pady=10)

    def play_game(self, user_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        user_result = self.determine_winner(user_choice, computer_choice)
        self.display_result(user_result, user_choice, self.user_result_label)

        computer_result = self.determine_winner(computer_choice, user_choice)
        self.display_result(computer_result, computer_choice, self.computer_result_label)

        self.update_score(user_result)

    def determine_winner(self, player_choice, opponent_choice):
        if player_choice == opponent_choice:
            return "Tie"
        elif (
            (player_choice == "Rock" and opponent_choice == "Scissors") or
            (player_choice == "Paper" and opponent_choice == "Rock") or
            (player_choice == "Scissors" and opponent_choice == "Paper")
        ):
            return "Win"
        else:
            return "Lose"

    def display_result(self, result, choice, label):
        label.config(text=f"{choice}\n{result}")

    def update_score(self, result):
        if result == "Win":
            self.user_score += 1
        elif result == "Lose":
            self.computer_score += 1

        self.score_label.config(text=f"Score: You {self.user_score} - {self.computer_score} Computer")

    def reset_game(self):
        self.user_result_label.config(text="")
        self.computer_result_label.config(text="")
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text=f"Score: You {self.user_score} - {self.computer_score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
