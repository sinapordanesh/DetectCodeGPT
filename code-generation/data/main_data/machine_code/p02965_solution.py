def count_sequences(N, M):
    MOD = 998244353

    def power(x, y):
        res = 1
        while y:
            if y % 2:
                res = res * x % MOD
            x = x * x % MOD
            y //= 2
        return res

    fact = [1] * (N + M + 1)
    inv_fact = [1] * (N + M + 1)
    for i in range(1, N + M):
        fact[i] = fact[i - 1] * i % MOD
        inv_fact[i] = power(fact[i], MOD - 2)

    def comb(x, y):
        if y < 0 or y > x:
            return 0
        return fact[x] * inv_fact[y] % MOD * inv_fact[x - y] % MOD

    ans = 0
    for i in range(N + 1):
        if i % 2 == 0:
            ans += comb(N + M - 1 - i, M) * comb(N, i) % MOD
        else:
            ans -= comb(N + M - 1 - i, M) * comb(N, i) % MOD
        ans %= MOD

    return ans

N, M = map(int, input().split())
print(count_sequences(N, M))