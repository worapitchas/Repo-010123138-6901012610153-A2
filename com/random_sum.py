import random

sum = 0    
i = 1    

while True:
    n = random.randint(-10,10)
    if n == -1:
        print("ผลรวมคือ:", sum)

        break

    else:
       sum = n+i  
    

