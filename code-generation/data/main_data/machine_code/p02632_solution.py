MOD = 10**9 + 7

def count_strings(K, S):
    n = len(S)
    
    fact = [1] * (n + K + 1)
    inv = [1] * (n + K + 1)
    
    for i in range(2, n + K):
        fact[i] = (fact[i - 1] * i) % MOD
        inv[i] = pow(fact[i], MOD - 2, MOD)
    
    def comb(n, k):
        return (fact[n] * inv[k] % MOD) * inv[n - k] % MOD
    
    total = 0
    for i in range(n + 1):
        total = (total + comb(n + K - i - 1, n - 1) * pow(25, K + i, MOD) % MOD) % MOD
    
    return total

K, S = map(int, input().split())
print(count_strings(K, S))