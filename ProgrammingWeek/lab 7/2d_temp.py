import random

temp = [ 
    [ 1, 2, 3, 4, 5, 6, 7], 
    [ 8, 9, 10, 11, 12, 13, 14], 
    [ 15, 16, 17, 18, 19, 20, 21], 
    [ 22, 23, 24, 25, 26, 27, 28]
]

def week_average(w):
    i = 0
    total_sum = 0 

    
    
    while i < len(temp[w]):
        total_sum = total_sum + temp[w][i] 
        i = i + 1
        
    
    average = total_sum / len(temp[w])
    return average

def week_max(w):

    i = 0
    day = 0
    max = temp[w][0]

    while i < len(temp[w]):
        if max < temp[w][day]:
            max = temp[w][day]
        i = i+1
        day = day + 1

    return max

def week_min(w):

    i = 0
    day = 0
    min = temp[w][0]

    while i < len(temp[w]):
        if min > temp[w][day]:
            min = temp[w][day]
        i = i+1
        day = day + 1

    return min

def overall_max():
    i = 0
    w = 0
    day = 0
    all_max = week_max(0)
    while i < len(temp):
        if all_max < week_max(w):
            all_max = week_max(w)
        i = i + 1
        day = day + 1
    return all_max

def overall_min():
    i = 0
    w = 0
    day = 0
    all_min = week_min(0)
    while i < len(temp):
        if all_min < week_min(w):
            all_min = week_min(w)
        i = i + 1
        day = day + 1
    return all_min

w = random.randint(0,3)

result_average = week_average(w)
print(result_average)

result_max = week_max(w)
print(result_max)

result_min = week_min(w)
print(result_min)

result_overall_max = overall_max()
print(result_overall_max)

result_overall_min = overall_min()
print(result_overall_min)