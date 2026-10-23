def is_perfect_number(n):
    if n <= 1:
        return False

    divisors_sum = 0
    i = 1
    while i < n:
        if n % i == 0:
            divisors_sum += i
        i += 1

    return divisors_sum == n


def find_perfect_numbers():
    print("Perfect numbers between 1 and 50:")
    num = 1
    while num <= 50:
        if is_perfect_number(num):
            print(num)
        num += 1


find_perfect_numbers()