MOD = 10**9 + 7

def sequences(N, M, L, R):
    def mod_inv(x):
        return pow(x, MOD - 2, MOD)

    def nCr(n, r):
        r = min(r, n - r)
        if r == 0:
            return 1
        res = 1
        for i in range(r):
            res *= n - i
            res *= mod_inv(i + 1)
            res %= MOD
        return res

    if N == M + 1:
        return 1

    ans = nCr(N - M + L - 1, L) * nCr(M + R - 1, R) % MOD
    ans -= nCr(N - M + L - 1, L - 1) * nCr(M + R - 1, R + 1) % MOD
    ans %= MOD

    return ans

# Read input values
N, M, L, R = map(int, input().split())

# Call the function and print the result
print(sequences(N, M, L, R))