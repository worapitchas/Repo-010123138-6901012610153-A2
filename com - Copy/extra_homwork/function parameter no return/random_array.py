import random

def make_array(amount):
    number = []
    while len(number) < amount:
        add = random.randint(10, 99)
        number.append(add)
    
    print(number)


make_array(21)