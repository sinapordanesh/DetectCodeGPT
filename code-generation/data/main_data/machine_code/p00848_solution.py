def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_ways(n, k, primes, index, memo):
    if n == 0 and k == 0:
        return 1
    if n <= 0 or k <= 0 or index >= len(primes):
        return 0
    
    if (n, k, index) in memo:
        return memo[(n, k, index)]
    
    count = count_ways(n - primes[index], k - 1, primes, index + 1, memo) + count_ways(n, k, primes, index + 1, memo)
    
    memo[(n, k, index)] = count
    
    return count

def find_prime_sets(n, k):
    primes = [i for i in range(2, n) if is_prime(i)]
    memo = {}
    return count_ways(n, k, primes, 0, memo)

def main():
    while True:
        n, k = map(int, input().split())
        if n == 0 and k == 0:
            break
        print(find_prime_sets(n, k))

if __name__ == "__main__":
    main()