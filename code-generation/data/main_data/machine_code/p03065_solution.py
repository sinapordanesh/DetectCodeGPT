import math

def prime_divisors(N, *coefficients):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    
    result = []
    for p in range(2, max(abs(coefficients[-1]), 2)):
        if is_prime(p):
            divisible = True
            for x in range(1, N+1):
                fx = sum([coefficients[i]*(p**i) for i in range(N+1)])
                if fx % p != 0:
                    divisible = False
                    break
            if divisible:
                result.append(p)
    return result

N = 2
coefficients = [7, -7, 14]
print(*prime_divisors(N, *coefficients))

N = 3
coefficients = [1, 4, 1, 5]
print(*prime_divisors(N, *coefficients))

N = 0
coefficients = [998244353]
print(*prime_divisors(N, *coefficients))