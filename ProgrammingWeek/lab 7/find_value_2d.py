number = [ [ 5, 7, 9 ],
[ 2, 4, 6 ],
[ 8, 3, 1 ] ]



def find_average():
    total_sum = 0
    count = 0  

    for row in number:
        
        for val in row:
            total_sum += val
            count += 1
            
   
    return total_sum / count


print(find_average())  

        


def find_max():

    max_val = number[0][0]
    for row in number:
        for val in row:
            if val > max_val:
                max_val = val
                
    return max_val

print(find_max()) 

def find_min():

    min_val = number[0][0]
    for row in number:
        for val in row:
            if val < min_val:
                min_val = val
                
    return min_val

print(find_min()) 
