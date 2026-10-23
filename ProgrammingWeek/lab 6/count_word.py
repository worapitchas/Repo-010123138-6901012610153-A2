def countWords(string):
    count = 0        
    in_word = False  
    
    i = 0
    while i < len(string):
        if string[i] != " ":
            if in_word == False:
                count += 1       
                in_word = True

        else:
            in_word = False
            
        i += 1  
        
    return count

print(countWords("Human and AI can make mistakes")) 
