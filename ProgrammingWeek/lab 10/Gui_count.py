import tkinter as tk

number = 1


root = tk.Tk()
root.title("GUI_COUNT")
root.geometry("300x300")

label = tk.Label(root, text=number, font=("Arial", 12))
label.pack(pady=60)

def increase_but():
    global number
    number += 1
    label.config(text=str(number))

btn = tk.Button(root, text="increase", command=increase_but)
btn.pack()


def decrease_but():
    global number
    number -= 1
    label.config(text=str(number))

btn = tk.Button(root, text="decrease", command=decrease_but)
btn.pack()

def reset_but():
    global number
    number = 0
    label.config(text=str(number))

btn = tk.Button(root, text="reset", command=reset_but)
btn.pack()

root.mainloop()