import random

def random_number():
    x = random.randint(-5, 5)
    print(x)
    
    if x < 0: 
        print("x is negative")
    elif x > 0:
        print("x is positive")
    else: 
        print("x is zero")

random_number()