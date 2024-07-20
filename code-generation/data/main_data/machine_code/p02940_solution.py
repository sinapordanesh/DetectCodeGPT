def distribute_balls(N, S):
    mod = 998244353
    fact = [1] * (3*N+1)
    inv = [1] * (3*N+1)
    inv_fact = [1] * (3*N+1)
    
    for i in range(1, 3*N+1):
        fact[i] = fact[i-1] * i % mod
        inv[i] = pow(i, mod-2, mod)
        inv_fact[i] = inv_fact[i-1] * inv[i] % mod
    
    def nCr(n, r):
        return fact[n] * inv_fact[r] * inv_fact[n-r] % mod
    
    ans = 1
    cnt = [0] * 3
    for s in S:
        if s == 'R':
            i = 0
        elif s == 'G':
            i = 1
        else:
            i = 2
        
        cnt[i] += 1
    
    for i in range(3):
        ans = ans * nCr(N*2, cnt[i]) % mod
    
    return ans

N = 3
S = "RRRGGGBBB"
print(distribute_balls(N, S))

N = 5
S = "BBRGRRGRGGRBBGB"
print(distribute_balls(N, S))