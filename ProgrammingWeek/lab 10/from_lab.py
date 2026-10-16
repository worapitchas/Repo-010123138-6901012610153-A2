import random  
import tkinter as tk


answer = random.randint(1, 100)

root = tk.Tk()
root.title("GUESS")
root.geometry("300x200")

entry = tk.Entry(root, width=25)
entry.pack(pady=10)


def guess_num():
    
    guess = int(entry.get())

    if guess < answer:
            label.config(text="Result: Higher!")
    elif guess > answer:
            label.config(text="Result: Lower!")
    else:
            label.config(text="Result: Correct!")


btn = tk.Button(root, text="Guess", command=guess_num)
btn.pack(pady=5)

label = tk.Label(root, text="Result: -")
label.pack(pady=15)

root.mainloop()