import random


def make_array(amount):
    number = []
    while len(number) < amount:
        add = random.randint(1, 100)
        number.append(add)
    return number


def find_median(num_list):
    num_list.sort()
    print(f"ข้อมูลหลังเรียงลำดับ: {num_list}")

    n = len(num_list)
    if n % 2 != 0:
        median = num_list[n // 2]
    else:
        mid1 = num_list[(n // 2) - 1]
        mid2 = num_list[n // 2]
        median = (mid1 + mid2) / 2

    return median


amount = int(input("Enter n: "))


data = make_array(amount)
print(f"ข้อมูลที่สุ่มได้: {data}")


result = find_median(data)
print(f"ค่ามัธยฐานคือ: {result}")


