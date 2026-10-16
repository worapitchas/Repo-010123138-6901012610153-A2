import random

number = []

def make_array():
    while len(number) < 21:
        add = random.randint(10,99)
        number.append(add)

make_array()

print(number)