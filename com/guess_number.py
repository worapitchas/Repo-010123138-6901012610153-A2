number = 67

while True:
    guess = int(input("ทายตัวเลขมาสิ : "))
    if guess > number:
        print("lower!")
    elif guess < number:
        print("higher!")
    if guess == number:
        break