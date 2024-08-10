def count_primes(datasets):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
    
    results = []
    for n in datasets:
        if n == 0:
            break
        count = 0
        for p in range(n+1, 2*n+1):
            if is_prime(p):
                count += 1
        results.append(count)
    
    return results

datasets = [1, 10, 13, 100, 1000, 10000, 100000]
print(*count_primes(datasets), sep='\n')