import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")
        self.root.geometry("400x400")
        self.root.config(bg="#f0f0f0")

        self.score_user = 0
        self.score_computer = 0

        self.title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        self.instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14), bg="#f0f0f0")
        self.instruction_label.pack(pady=10)

        self.choice_var = tk.StringVar(value="Rock")  # Default choice
        choices = ["Rock", "Paper", "Scissors"]

        # Radio buttons for user choice
        for choice in choices:
            tk.Radiobutton(root, text=choice, variable=self.choice_var, value=choice, font=("Arial", 12), bg="#f0f0f0").pack(anchor='w')

        self.play_button = tk.Button(root, text="Play", command=self.play_game, font=("Arial", 14), bg="#4CAF50", fg="white", relief="raised")
        self.play_button.pack(pady=20)

        self.result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="#f0f0f0")
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 14), bg="#f0f0f0")
        self.score_label.pack(pady=10)

        self.play_again_button = tk.Button(root, text="Play Again", command=self.reset_game, font=("Arial", 14), bg="#2196F3", fg="white", relief="raised")
        self.play_again_button.pack(pady=10)

    def play_game(self):
        user_choice = self.choice_var.get()
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        
        # Determine the winner
        if user_choice == computer_choice:
            result = "It's a Tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Scissors" and computer_choice == "Paper") or \
             (user_choice == "Paper" and computer_choice == "Rock"):
            result = "You Win!"
            self.score_user += 1
        else:
            result = "You Lose!"
            self.score_computer += 1
        
        self.result_label.config(text=f"You chose {user_choice}\nComputer chose {computer_choice}\n{result}")
        self.update_score()

    def update_score(self):
        self.score_label.config(text=f"Score - You: {self.score_user} | Computer: {self.score_computer}")

    def reset_game(self):
        self.score_user = 0
        self.score_computer = 0
        self.update_score()
        self.result_label.config(text="")
        self.choice_var.set("Rock")  # Reset to default choice

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()