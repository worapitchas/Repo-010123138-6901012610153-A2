number = [300,800,600,400,300,900,550,650,420,601]
index = 0

while index < len(number):
    val = number[index]

    if val > 500:
        print(f"{val} more than 500")

    index = index + 1
