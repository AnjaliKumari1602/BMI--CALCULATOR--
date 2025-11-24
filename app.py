import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        height = float(entry_height.get()) / 100   # Convert cm → meters
        weight = float(entry_weight.get())

        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=f"Your BMI is {bmi} ({category})")

    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers!")

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x300")
root.resizable(False, False)

tk.Label(root, text="BMI CALCULATOR", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Enter height (cm):").pack()
entry_height = tk.Entry(root)
entry_height.pack(pady=5)

tk.Label(root, text="Enter weight (kg):").pack()
entry_weight = tk.Entry(root)
entry_weight.pack(pady=5)

tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Debug: help ensure the window appears on top (useful if window opens behind others)
print("Starting BMI GUI...")
root.update()
try:
    root.lift()
    root.attributes('-topmost', True)
    # turn off topmost after a short delay so the window can behave normally
    root.after(1000, lambda: root.attributes('-topmost', False))
except Exception:
    # attributes/lift might not be supported in some environments; ignore safely
    pass

root.mainloop()
