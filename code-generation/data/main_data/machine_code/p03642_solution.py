import math

def min_operations(N, cards):
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True
    
    max_prime = max(cards)
    
    primes = []
    for i in range(2, max_prime+1):
        if is_prime(i):
            primes.append(i)
    
    operations = 0
    for prime in primes:
        if prime >= 3:
            for i in range(len(cards)-prime+1):
                if cards[i] == 1:
                    for j in range(i, i+prime):
                        cards[j] = 1 - cards[j]
                    operations += 1
    
    return operations

# Sample Input
print(min_operations(2, [4, 5])) # Output: 2
print(min_operations(9, [1, 2, 3, 4, 5, 6, 7, 8, 9])) # Output: 3
print(min_operations(2, [1, 10000000])) # Output: 4