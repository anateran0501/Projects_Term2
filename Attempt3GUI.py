import random
import tkinter as tk
from tkinter import messagebox

class GuessingGameGUI:
    def __init__(self):
        self.number_to_guess = random.randint(0, 199)
        self.attempts = 5
        self.attempt_count = 0

        self.root = tk.Tk()
        self.root.title("Guessing Game")
        
        self.label = tk.Label(self.root, text="Welcome to the Guessing Game!")
        self.label.pack()

        self.info_label = tk.Label(self.root, text="I'm thinking of a number between 0 and 199.\nYou have 5 chances to guess the number.")
        self.info_label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.button = tk.Button(self.root, text="Submit", command=self.check_guess)
        self.button.pack()

    def check_guess(self):
        guess = int(self.entry.get())
        self.attempt_count += 1

        if guess == self.number_to_guess:
            messagebox.showinfo("Congratulations", f"You've guessed the number in {self.attempt_count} attempts!")
            self.root.destroy()
        else:
            if abs(guess - self.number_to_guess) > 15:
                messagebox.showinfo("Incorrect", "You're far from the number.")
            elif abs(guess - self.number_to_guess) <= 15:
                messagebox.showinfo("Incorrect", "You're close, but not quite there.")
            else:
                messagebox.showinfo("Incorrect", "You're very close!")

            if self.attempt_count == self.attempts:
                messagebox.showinfo("Game Over", f"Sorry, you've used all your attempts. The number was {self.number_to_guess}.")
                self.root.destroy()

        self.entry.delete(0, tk.END)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = GuessingGameGUI()
    game.run()