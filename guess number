import tkinter as tk
import random

root = tk.Tk()
root.title("Guess the number")
root.geometry("400x300")
title_label = tk.Label(root, text="Guess the number", font=("Arial", 18))
title_label.pack(pady=10)
prompt_label = tk.Label(root, text="Enter a number (1-100):")
prompt_label.pack()
guess_entry = tk.Entry(root, width=10, justify="center")
guess_entry.pack(pady=5)
result_label = tk.Label(root, text="Good luck", font=("Arial:,14"))
result_label.pack(pady=10)
secret = random.randint(1,100)
def check_guess():
    text = guess_entry.get().strip()
    if not text.isdigit():
        result_label.config(text="Please enter a number")
    guess = int(text)
    if guess < secret:
        result_label.config(text="Too low")
    elif guess > secret:
        result_label.config(text="Too high")
    else:
        result_label.config(text="Correct")
check_btn = tk.Button(root, text="Check", command=check_guess)
check_btn.pack(pady=5)
def reset_game():
    global secret
    secret = random.randint(1,100)
    result_label.config(text="New game, guess again.")
    guess_entry.delete(0, tk.END)
reset_btn = tk.Button(root, text="Reset", command=reset_game)
reset_btn.pack(pady=5)



root.mainloop()
