import random

number = []

def make_number(amount):
    while len(number) < amount:

        x = random.randint(1,100)
        y = random.randint(1,5)

        result = x**y
        number.append(result)


amount = int(input("enter amount of number : "))

make_number(amount)
print(number)