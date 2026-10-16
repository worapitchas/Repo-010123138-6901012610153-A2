number = [100,200,300,400,500]

def find_average_array():
    sum = 0
    i = 0
    while i < len(number):
        sum += number[i]
        i += 1
    average = sum / len(number)
    return average

result_average = find_average_array()

def find_variance_array():
    avg = find_average_array()  
    sum_sq_diff = 0
    i = 0

    while i < len(number):
        diff = number[i] - avg  
        sum_sq_diff += diff * diff  
        i += 1

    variance = sum_sq_diff / len(number)  
    return variance

print(find_variance_array())