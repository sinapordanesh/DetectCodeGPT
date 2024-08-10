def pair_of_primes(N):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    primes = [i for i in range(2, N+1) if is_prime(i)]
    pairs = 0
    for i in range(len(primes)//2):
        pairs += 1
    return pairs

print(pair_of_primes(1))
print(pair_of_primes(4))
print(pair_of_primes(7))
print(pair_of_primes(51))