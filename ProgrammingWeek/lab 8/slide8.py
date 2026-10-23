def sum_2Dn(number):
    sum_total = 0  
    i = 0  
    
    while (i < len(number)):  
        j = 0  
        while (j < len(number[i])): 
            sum_total = sum_total + number[i][j]
            j = j + 1
        i = i + 1
        
    return sum_total 

m = [
    [5, 7, 9], 
    [2, 4, 6], 
    [8, 3, 1]
]

print(sum_2Dn(m))
