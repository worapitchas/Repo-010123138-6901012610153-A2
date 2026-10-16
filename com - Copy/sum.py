n = int(input("กรอกค่า n: "))

sum = 0    
i = 1    

while i <= n:
    sum = sum + i  
    i = i + 1     

print("ผลรวมตั้งแต่ 1 ถึง", n, "คือ:", sum)