def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def nth_prime_in_arithmetic_sequence(a, d, n):
    count = 0
    current_num = a
    while count < n:
        if is_prime(current_num):
            count += 1
        current_num += d
    return current_num - d

while True:
    a, d, n = map(int, input().split())
    if a == 0 and d == 0 and n == 0:
        break
    print(nth_prime_in_arithmetic_sequence(a, d, n))