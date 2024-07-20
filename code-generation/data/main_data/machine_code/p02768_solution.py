def count_bouquets(n, a, b):
    MOD = 10**9 + 7
    
    def comb(n, r):
        if r > n - r:
            r = n - r
        res = 1
        for i in range(1, r + 1):
            res = (res * (n - i + 1) // i) % MOD
        return res
    
    total = pow(2, n, MOD) - 1
    total -= comb(n, a)
    total -= comb(n, b)
    
    return (total % MOD)

# Sample Input 1
n = 4
a = 1
b = 3
print(count_bouquets(n, a, b))

# Sample Input 2
n = 1000000000
a = 141421
b = 173205
print(count_bouquets(n, a, b))