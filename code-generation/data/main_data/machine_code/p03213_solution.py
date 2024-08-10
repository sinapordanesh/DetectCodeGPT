import math

def count_shichi_go_numbers(N):
    def get_prime_factors(n):
        factors = {}
        while n % 2 == 0:
            factors[2] = factors.get(2, 0) + 1
            n = n // 2
        for i in range(3, int(math.sqrt(n))+1, 2):
            while n % i == 0:
                factors[i] = factors.get(i, 0) + 1
                n = n // i
        if n > 2:
            factors[n] = factors.get(n, 0) + 1
        return factors
    
    def num_divisors(n):
        prime_factors = get_prime_factors(n)
        result = 1
        for val in prime_factors.values():
            result *= (val+1)
        return result
        
    factorial = math.factorial(N)
    count = 0
    for i in range(1, factorial+1):
        if num_divisors(i) == 75:
            count += 1
    return count

N = int(input())
print(count_shichi_go_numbers(N))