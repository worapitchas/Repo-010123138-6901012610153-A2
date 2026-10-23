import tkinter as tk

root = tk.Tk()
root.title("convert_temp")
root.geometry("300x200")

entry = tk.Entry(root, width=25)
entry.pack(pady=15)


def convert():
    user_input = float(entry.get())  
    F = (user_input * 1.8) + 32
    label.config(text=f"Result: {F:.2f} °F", fg="black")
   

btn = tk.Button(root, text="Convert", command=convert)
btn.pack(pady=5)

label = tk.Label(root, text="Result: -")
label.pack(pady=15)

root.mainloop()