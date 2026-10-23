number = [100,200,300,400,500]

def find_max_array():
    
    max = number[0]
    max_index = 0
    i = 1
    while i < len(number):
        if max < number[i]:
            max = number[i]
            max_index = i
        i+=1
    
    return max_index




def find_min_array():
    
    min = number[0]
    i = 1
    min_index = 0
    while i < len(number):
        if min > number[i]:
            min = number[i]
            min_index = i
        i+=1
    return min_index



result_min = find_min_array()
result_max = find_max_array()
print(result_max)
print(result_min)
