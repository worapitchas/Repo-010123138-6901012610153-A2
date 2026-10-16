def search_str(string):
    find = (input("enter letter: "))

    i = 0
    

    while i < len(string):
        if find == string[i]:
            index_search = i
        i+=1
    return index_search
        
string = "meow"

result_letter = search_str(string)
print(result_letter)
