import random

number = random.randint(1,100)

while True:
    guess = int(input("ทายตัวเลขจาก 1-100 "))
    if guess > number:
        print("lower")
    elif guess < number:
        print("higher")
    elif guess == 0:
        break
    elif guess == number:
        print("yay")
    else:
        print("ไม่ตรงตามเงื่อนไข")