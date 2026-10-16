def find_prime_1_to_100():
    print("Prime numbers between 1 and 100:")
    num = 2  

    while num <= 100:
        is_prime = True
        i = 2

        while i < num:
            if num % i == 0:
                is_prime = False  
                break
            i = i + 1

        if is_prime:
            print(num, end=" ")

        num = num + 1


find_prime_1_to_100()