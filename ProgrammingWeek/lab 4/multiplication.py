def multiplication_table():
    num = int(input("Enter number: "))
    i = 1 
    while i <= 12:  
        print(f"{num} x {i} = {num * i}")
        i += 1  

multiplication_table()