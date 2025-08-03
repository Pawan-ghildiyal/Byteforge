import tkinter as tk
import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    result_var.set(f"🎲 Dice 1: {die1}    🎲 Dice 2: {die2}")

root = tk.Tk()
root.title("Dice Rolling Simulator")
root.geometry("300x200")
root.resizable(False, False)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 16), pady=20)
result_label.pack()

roll_button = tk.Button(root, text="Roll Dice", font=("Arial", 14), command=roll_dice)
roll_button.pack(pady=10)

result_var.set("Click 'Roll Dice' to start")

root.mainloop()
