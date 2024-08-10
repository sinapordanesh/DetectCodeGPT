def number_of_different_grids(N, M):
    mod = 998244353
    fact = [1] * (N + M + 1)
    inv = [1] * (N + M + 1)
    invfact = [1] * (N + M + 1)
    for i in range(2, N + M + 1):
        fact[i] = fact[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        invfact[i] = invfact[i - 1] * inv[i] % mod
    
    ans = 0
    for i in range(N):
        ans += fact[N+M-1] * invfact[i] % mod * invfact[N+M-1-i] % mod * invfact[M-1] % mod
        ans %= mod
    
    return ans

# Sample Input 1
print(number_of_different_grids(1, 2))

# Sample Input 2
print(number_of_different_grids(2, 3))

# Sample Input 3
print(number_of_different_grids(10, 7))

# Sample Input 4
print(number_of_different_grids(314159, 265358))