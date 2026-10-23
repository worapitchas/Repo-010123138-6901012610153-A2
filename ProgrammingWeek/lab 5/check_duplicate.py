number = [100, 200, 300, 400, 500]  

def has_duplicates():
    i = 0
    while i < len(number) - 1:
        j = i + 1 
        while j < len(number):
            if number[i] == number[j]:  
                return True
            j += 1
        i += 1
    return False  

print(has_duplicates())