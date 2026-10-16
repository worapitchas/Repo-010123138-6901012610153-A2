my_array = [ [ 5, 7, 9 ],
[ 2, 4, 6 ],
[ 8, 3, 1 ] ]

def check_val(number, find):
    for row in number:
        for val in row:
            if find == val:
                return True  
                
    return False
find = int(input("enter number: "))


print(check_val(my_array,find))