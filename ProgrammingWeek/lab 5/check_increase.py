number = [100, 200, 300, 400, 500]  


def is_increasing_array():
    i = 0
    while i < len(number) - 1:
        if number[i] > number[i + 1]:  
            return False  
        i += 1

    return True  

print(is_increasing_array())
