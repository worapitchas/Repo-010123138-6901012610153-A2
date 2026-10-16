import random

number = []

while len(number) < 10:

    x = random.randint(1,100)
    y = random.randint(1,5)

    result = x**y
    number.append(result)

print(number)