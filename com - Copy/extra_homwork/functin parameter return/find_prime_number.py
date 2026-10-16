def find_prime_number(lenght):
    prime_number = []
    num = 2
    
    while num <= lenght:
        divisor = 2
        is_prime = True

        while divisor < num:
            if num % divisor == 0:
                is_prime = False
                break
            divisor = divisor + 1

        if is_prime:
            prime_number.append(num)

        num = num + 1
        
    return prime_number

lenght = int(input("enter number : "))
result = find_prime_number(lenght)
print(result)