def possible_ways(N, K):
    MOD = 998244353
    fact = [1] * (K+1)
    inv = [1] * (K+1)
    for i in range(2, K+1):
        fact[i] = (fact[i-1] * i) % MOD
        inv[i] = pow(fact[i], MOD-2, MOD)
    
    def nCr(n, r):
        return (fact[n] * inv[r] * inv[n-r]) % MOD
    
    if N == 1:
        if K % 2 == 0:
            return 2
        else:
            return 1
    elif N == 2:
        return (2 * pow(2, K-1, MOD)) % MOD
    elif N >= 3:
        ans = 0
        for i in range(min(K, N*2-1) // 2 + 1):
            ans = (ans + nCr(K-1, 2*i) * nCr(K-2-2*i+N-1, N-1)) % MOD
        return ans

N, K = map(int, input().split())
print(possible_ways(N, K))