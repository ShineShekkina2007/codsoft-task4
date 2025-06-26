import tkinter as tk
import random

class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.configure(bg="skyblue")
        self.root.geometry("500x400")

        self.choices = ["Rock", "Paper", "Scissors"]
        self.user_score = 0
        self.computer_score = 0

        # Labels
        self.title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"), bg="skyblue")
        self.title.pack(pady=20)

        self.result = tk.Label(root, text="", font=("Arial", 16), bg="skyblue")
        self.result.pack(pady=10)

        self.score = tk.Label(root, text="User: 0  |  Computer: 0", font=("Arial", 14), bg="skyblue")
        self.score.pack(pady=10)

        # Buttons
        button_frame = tk.Frame(root, bg="skyblue")
        button_frame.pack(pady=20)

        for choice in self.choices:
            btn = tk.Button(
                button_frame,
                text=choice,
                font=("Arial", 14),
                bg="lightpink",
                width=10,
                command=lambda ch=choice: self.play(ch)
            )
            btn.pack(side=tk.LEFT, padx=10)

        self.quit_btn = tk.Button(root, text="Quit", font=("Arial", 12), bg="salmon", command=root.quit)
        self.quit_btn.pack(pady=20)

    def play(self, user_choice):
        computer_choice = random.choice(self.choices)

        if user_choice == computer_choice:
            outcome = "It's a Tie!"
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Paper" and computer_choice == "Rock") or
            (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            outcome = "You Win!"
            self.user_score += 1
        else:
            outcome = "Computer Wins!"
            self.computer_score += 1

        self.result.config(text=f"You chose {user_choice} | Computer chose {computer_choice}\n{outcome}")
        self.score.config(text=f"User: {self.user_score}  |  Computer: {self.computer_score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = RPSGame(root)
    root.mainloop()
