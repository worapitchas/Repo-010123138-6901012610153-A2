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


def more_than_average():
    i = 0
    count = 0
    while i < len(number):
        if result_average < number[i]:
            count = count + 1
        i += 1

    return count

result_count = more_than_average()
print(result_count)