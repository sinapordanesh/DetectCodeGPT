def door_to_open(a, b):
    def prime_factors(n):
        i = 2
        factors = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
        return factors

    def key_number(num):
        primes = prime_factors(num)
        largest = max(primes)
        total = sum(primes) - largest
        return largest - total

    if key_number(a) > key_number(b):
        return 'a'
    else:
        return 'b'