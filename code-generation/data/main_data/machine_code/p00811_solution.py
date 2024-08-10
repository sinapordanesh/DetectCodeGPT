def find_most_suitable_width_height():
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes_less_than(num):
        primes = []
        for i in range(2, num):
            if is_prime(i):
                primes.append(i)
        return primes

    def get_max_product_primes(m, a, b):
        primes = get_primes_less_than(m)
        max_product = 0
        width = 0
        height = 0
        for i in range(len(primes)):
            for j in range(i, len(primes)):
                if primes[i] * primes[j] <= m and a / b <= primes[i] / primes[j] <= 1:
                    if primes[i] * primes[j] > max_product:
                        max_product = primes[i] * primes[j]
                        width = primes[i]
                        height = primes[j]
        return width, height

    while True:
        m, a, b = map(int, input().split())
        if m == 0 and a == 0 and b == 0:
            break
        width, height = get_max_product_primes(m, a, b)
        print(width, height)

find_most_suitable_width_height()