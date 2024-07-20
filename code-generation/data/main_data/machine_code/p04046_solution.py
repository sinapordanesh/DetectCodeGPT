def count_ways_to_bottom_right(H, W, A, B):
    MOD = 10**9 + 7
    fact = [1] * (H + W)
    inv = [1] * (H + W)
    for i in range(1, H + W):
        fact[i] = fact[i - 1] * i % MOD
        inv[i] = pow(fact[i], MOD - 2, MOD)

    def comb(n, r):
        return fact[n] * inv[n - r] * inv[r] % MOD

    ans = 0
    for i in range(H - A):
        ans += comb(i + B - 1, B - 1) * comb(H - i + W - B - 2, W - B - 1)
        ans %= MOD
    return ans

# Sample Input 1
print(count_ways_to_bottom_right(2, 3, 1, 1))

# Sample Input 2
print(count_ways_to_bottom_right(10, 7, 3, 4))

# Sample Input 3
print(count_ways_to_bottom_right(100000, 100000, 99999, 99999))

# Sample Input 4
print(count_ways_to_bottom_right(100000, 100000, 44444, 55555))