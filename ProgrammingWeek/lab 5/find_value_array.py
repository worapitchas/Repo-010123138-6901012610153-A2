number = [100,200,300,400,500]

def find_max_array():
    
    max = number[0]
    i = 1
    while i < len(number):
        if max < number[i]:
            max = number[i]
        i+=1
    return max

def find_min_array():
    
    min = number[0]
    i = 1
    while i < len(number):
        if min > number[i]:
            min = number[i]
        i+=1
    return min

def find_average_array():
    sum = 0
    i = 0
    while i < len(number):
        sum += number[i]
        i += 1
    average = sum / len(number)
    return average



result_average = find_average_array()
result_min = find_min_array()
result_max = find_max_array()
print(result_max)
print(result_min)
print(result_average)