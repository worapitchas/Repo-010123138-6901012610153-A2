import tkinter as tk

root = tk.Tk()
root.title("GUI TEXT")
root.geometry("500x500")

entry = tk.Entry(root, width=25)
entry.pack(pady=15)

def count_char():
    user_input = entry.get()
    Vowel = len(user_input)
    label1.config(text=f"จำนวนตัวอักษร: {Vowel} ตัว")

def count_Vol():
    user_input = entry.get().lower()  
    vowels = "aeiou"
    vowel_count = 0 

    for char in user_input:
        if char in vowels:
            vowel_count += 1

    label2.config(text=f"จำนวนสระ: {vowel_count} ตัว")

def check_palindrome():
    
    text = entry.get().lower()

    
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text  

    
    if text == reversed_text:
        label3.config(text="เป็น panlindrome มั้ย: ใช่")
    else:
        label3.config(text="เป็น panlindrome มั้ย: ไม่")
   

btn1 = tk.Button(root, text="Count_character", command=count_char)
btn1.pack(pady=5)

label1 = tk.Label(root, text="Result: -")
label1.pack(pady=15)

btn2 = tk.Button(root, text="Count_Vowels", command=count_Vol)
btn2.pack(pady=10)

label2 = tk.Label(root, text="Result: -")
label2.pack(pady=20)

btn3 = tk.Button(root, text="Count_Vowels", command=check_palindrome)
btn3.pack(pady=15)

label3 = tk.Label(root, text="Result: -")
label3.pack(pady=25)

root.mainloop()