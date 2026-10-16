n = int(input("ป้อนตัวเลข: "))
factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i  

print(f"ค่าของ {n}! คือ {factorial}")