import random



def make_number(amount):
    number = []
    while len(number) < amount:

        x = random.randint(1,100)
        y = random.randint(1,5)

        result = x**y
        number.append(result)
    return number

amount = int(input("enter amount of number : "))


result = make_number(amount)
print(result)