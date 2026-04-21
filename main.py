import tkinter as tk
from tkinter import messagebox

instructions = 0
rate = 0

def click():
    global instructions
    instructions += 1
    update_label()

def update_label():
    label.config(text=f"Instructions: {hex(instructions)}")

def buy_generator(cost, increment, info):
    global instructions, rate
    if instructions >= cost:
        instructions -= cost
        rate += increment
        update_label()
        messagebox.showinfo("Architecture Info", info)

def auto_increment():
    global instructions
    instructions += rate
    update_label()
    root.after(1000, auto_increment)

root = tk.Tk()
root.title("Instruction Clicker")

label = tk.Label(root, text="Instructions: 0x0", font=("Arial", 16))
label.pack()

click_btn = tk.Button(root, text="⚙️ Processor", font=("Arial", 20), command=click)
click_btn.pack()

tk.Button(root, text="Buy MOV Unit (10)",
          command=lambda: buy_generator(10, 1,
          "ARM: mov x0, x1\nx86: mov rax, rbx")).pack()

tk.Button(root, text="Buy ADD Unit (50)",
          command=lambda: buy_generator(50, 5,
          "ARM: add x0, x1, x2\nx86: add rax, rbx")).pack()

tk.Button(root, text="Buy IF Unit (100)",
          command=lambda: buy_generator(100, 10,
          "ARM: b.eq\nx86: je")).pack()

auto_increment()
root.mainloop()