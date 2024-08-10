def colorful_balls(N, K):
    MOD = 10**9 + 7
    fact = [1] * (N*K+1)
    for i in range(1, N*K+1):
        fact[i] = fact[i-1] * i % MOD
    
    inv_fact = [1] * (N*K+1)
    inv_fact[N*K] = pow(fact[N*K], MOD-2, MOD)
    for i in range(N*K-1, 0, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
    
    def nCr(n, r):
        return fact[n] * inv_fact[r] * inv_fact[n-r] % MOD
    
    ans = 0
    for i in range(1, N+1):
        ans += nCr(N, i) * nCr(N-1, i-1)
        ans %= MOD
    
    return ans

N, K = map(int, input().split())
print(colorful_balls(N, K))