def max_divisors(A, B):
    import math
    
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    
    def count_coprime_divisors(n):
        count = 0
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                if n // i == i or gcd(n // i, i) == 1:
                    count += 1
                else:
                    count += 2
        return count
    
    return min(count_coprime_divisors(A), count_coprime_divisors(B))

# Sample Input 1
print(max_divisors(12, 18))

# Sample Input 2
print(max_divisors(420, 660))

# Sample Input 3
print(max_divisors(1, 2019))