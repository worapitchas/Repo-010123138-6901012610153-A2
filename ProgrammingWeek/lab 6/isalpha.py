def custom_isalpha(string):
    if len(string) == 0:
        return False
        
    i = 0
    while i < len(string):
        char = string[i]
        if not (('a' <= char <= 'z') or ('A' <= char <= 'Z')):
            return False  
        i += 1
    return True


print(custom_isalpha("NBA"))      
print(custom_isalpha("lab6_2026"))   
