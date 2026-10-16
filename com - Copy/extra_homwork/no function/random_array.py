import random

number = []

while len(number) < 21:
    add = random.randint(10,99)
    number.append(add)

print(number)