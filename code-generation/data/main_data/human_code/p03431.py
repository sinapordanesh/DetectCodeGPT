mod = 998244353
def comb(n, r):
    if n < r:return 0
    if n < 0 or r < 0:return 0
    return fa[n] * fi[r] % mod * fi[n - r] % mod
n, k = map(int, input().split())
fa = [1] * (k + 1)
fi = [1] * (k + 1)
for i in range(1, k + 1):
    fa[i] = fa[i - 1] * i % mod
    fi[i] = pow(fa[i], mod - 2, mod)
ans = 0
for i in range(k - n + 1):
    ans += comb(k - 1, n + i - 1)
    ans %= mod
print(ans)