import random

number = []

def make_array(amount):

    print(f"{amount} ตัว")

    while len(number) < amount:
        add = random.randint(1,100)
        number.append(add)

amount = int(input("enter n: "))

make_array(amount)

print(number)

def find_median():

    number.sort()

    print(f"ข้อมูลหลังเรียงลำดับ: {number}")


    n = len(number)
    if n % 2 != 0:
        
        median = number[n // 2]
    else:
        mid1 = number[(n // 2) - 1]
        mid2 = number[n // 2]
        median = (mid1 + mid2) / 2

    print(f"ค่ามัธยฐานคือ: {median}")

find_median()