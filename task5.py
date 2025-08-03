import tkinter as tk
from tkinter import ttk

def convert():
    try:
        value = float(entry.get())
        conv = conversion_type.get()

        if conv == "cm to inch":
            result = value / 2.54
        elif conv == "inch to cm":
            result = value * 2.54
        elif conv == "kg to lb":
            result = value * 2.20462
        elif conv == "lb to kg":
            result = value / 2.20462
        elif conv == "C to F":
            result = (value * 9/5) + 32
        elif conv == "F to C":
            result = (value - 32) * 5/9
        else:
            result = "Invalid"
        
        result_var.set(f"Result: {round(result, 2)}")
    except ValueError:
        result_var.set("Enter a valid number")

root = tk.Tk()
root.title("Unit Converter")
root.geometry("350x250")
root.resizable(False, False)

tk.Label(root, text="Enter value:", font=("Arial", 12)).pack(pady=5)
entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=5)

tk.Label(root, text="Select conversion type:", font=("Arial", 12)).pack(pady=5)
conversion_type = ttk.Combobox(root, font=("Arial", 12), state="readonly")
conversion_type['values'] = [
    "cm to inch", "inch to cm",
    "kg to lb", "lb to kg",
    "C to F", "F to C"
]
conversion_type.current(0)
conversion_type.pack(pady=5)

tk.Button(root, text="Convert", font=("Arial", 12), command=convert).pack(pady=10)

result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, font=("Arial", 14)).pack(pady=10)

root.mainloop()
