import random

number = []

while len(number) < 11:
    add = random.randint(100,1000)
    number.append(add)

print(number)

index = 0

while index < len(number):
    val = number[index]

    if val > 800:
        print(f"{val} more than 500")

    index = index + 1

