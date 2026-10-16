def search_str(string):
    find = input("enter letter: ")

   
    i = len(string) - 1
    
    
    index_search = -1

    while i > -1:
        if find == string[i]:
            index_search = i
        i -= 1
        
    return index_search
        
string = "meow"
result_letter = search_str(string)
print(result_letter)
