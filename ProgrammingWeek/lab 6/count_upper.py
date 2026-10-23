def count_upper(string):
    count = 0
    i = 0
    while i < len(string):
        char = string[i]
        if 'A' <= char <= 'Z':
            count += 1
        i += 1
    return count


print(count_upper("BTS Mrt")) 
