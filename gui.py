import tkinter as tk
from tkinter import messagebox
from subnet import subnet_calculator


# -----------------------------
# Calculate Function
# -----------------------------
def calculate():

    ip = ip_entry.get().strip()
    prefix = prefix_entry.get().strip()

    result = subnet_calculator(ip, prefix)

    if result is None:
        messagebox.showerror("Error", "Invalid IP Address or Prefix!")
        return

    result_box.config(state="normal")
    result_box.delete("1.0", tk.END)

    for key, value in result.items():
        result_box.insert(tk.END, f"{key:<20}: {value}\n")

    result_box.config(state="disabled")


# -----------------------------
# Clear Function
# -----------------------------
def clear():

    ip_entry.delete(0, tk.END)
    prefix_entry.delete(0, tk.END)

    result_box.config(state="normal")
    result_box.delete("1.0", tk.END)
    result_box.config(state="disabled")


# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()

root.title("NetCalc Lite")
root.geometry("600x500")
root.resizable(False, False)

# -----------------------------
# Title
# -----------------------------
title = tk.Label(
    root,
    text="NetCalc Lite",
    font=("Arial", 22, "bold"),
    fg="blue"
)

title.pack(pady=10)

subtitle = tk.Label(
    root,
    text="Simple IPv4 Subnet Calculator",
    font=("Arial", 11)
)

subtitle.pack()

# -----------------------------
# IP Address
# -----------------------------
tk.Label(root, text="IP Address", font=("Arial", 11)).pack(pady=5)

ip_entry = tk.Entry(root, width=35, font=("Arial", 11))
ip_entry.pack()

# -----------------------------
# Prefix
# -----------------------------
tk.Label(root, text="Prefix Length", font=("Arial", 11)).pack(pady=5)

prefix_entry = tk.Entry(root, width=10, font=("Arial", 11))
prefix_entry.pack()

# -----------------------------
# Buttons
# -----------------------------
frame = tk.Frame(root)
frame.pack(pady=15)

tk.Button(
    frame,
    text="Calculate",
    bg="green",
    fg="white",
    width=12,
    command=calculate
).grid(row=0, column=0, padx=5)

tk.Button(
    frame,
    text="Clear",
    bg="orange",
    width=12,
    command=clear
).grid(row=0, column=1, padx=5)

tk.Button(
    frame,
    text="Exit",
    bg="red",
    fg="white",
    width=12,
    command=root.destroy
).grid(row=0, column=2, padx=5)

# -----------------------------
# Results
# -----------------------------
result_box = tk.Text(
    root,
    width=65,
    height=15,
    font=("Consolas", 10)
)

result_box.pack(pady=10)

result_box.config(state="disabled")

# -----------------------------
# Start
# -----------------------------
root.mainloop()