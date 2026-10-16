import random

number =[]

def make_array():
    

    while len(number) < 11:
        add = random.randint(100,1000)
        number.append(add)

make_array()

print(number)

def check_val(index):
    
        val = number[index]

        if val > 800:
            print(f"{val} more than 500")
        else:
            print(f"{val} is not more than 500")
        

index = int(input("choose number order"))
check_val(index)

