def custom_equals(str1, str2):
    
    if len(str1) != len(str2):
        return False
        
    i = 0
    while i < len(str1):
        if str1[i] != str2[i]:
            return False  
        i += 1
    return True


print(custom_equals("cat", "cat"))  
print(custom_equals("cat", "dog"))  