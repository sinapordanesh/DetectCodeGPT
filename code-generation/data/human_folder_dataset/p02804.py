mod = 10 ** 9 + 7
N = 10 ** 5 + 1
fact = [1] * (N + 1)
ifact = [1] * (N + 1)

for i in range(N):
    fact[i + 1] = fact[i] * (i + 1) % mod
    ifact[i + 1] = pow(fact[i + 1], mod - 2, mod)


def comb(x, y):
    if y < 0 or y > x:
        return 0
    return (fact[x] * ifact[x - y] * ifact[y]) % mod


n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
ar = sorted(a, reverse=True)

ans = 0
for i in range(k - 1, n):
    ans += a[i] * comb(i, k - 1) % mod
    ans -= ar[i] * comb(i, k - 1) % mod
    ans %= mod

print(ans)
