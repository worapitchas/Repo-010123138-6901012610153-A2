import random

number =[]

def make_array():
    

    while len(number) < 11:
        add = random.randint(100,1000)
        number.append(add)

make_array()
print(number)

def check_val():
    index = 0

    while index < len(number):
        val = number[index]

        if val > 800:
            print(f"{val} more than 500")

        index = index + 1

check_val()