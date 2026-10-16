import random


def make_array(amount):
    number = []
    while len(number) < amount:
        add = random.randint(100, 1000)
        number.append(add)
    return number


def check_val(num_list, index):
    val = num_list[index]
    if val > 800:
        return f"{val} is more than 800"
    else:
        return f"{val} is not more than 800"


number = make_array(10)
print("ข้อมูลทั้งหมดในอาร์เรย์:", number)

index = int(input("choose number order (0-9): "))


result = check_val(number, index)
print(result)