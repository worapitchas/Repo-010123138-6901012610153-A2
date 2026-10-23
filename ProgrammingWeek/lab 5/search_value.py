number = [100,200,300,400,500]

def search_val():
    find = int(input("enter value: "))

    i = 0
    index_search = 0

    while i < len(number):
        if find == number[i]:
            index_search = i
        i+=1
    return index_search
        


result_index = search_val()
print(result_index)
