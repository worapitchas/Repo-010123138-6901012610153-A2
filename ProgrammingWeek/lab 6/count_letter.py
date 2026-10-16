def countchar(letter,word):
    word = word.lower()
    count = 0
    i = 0
    while i < len(word):
        if letter == word[i]:
            count += 1
        i+=1
    return count

print(countchar("a","AaAa"))
        
