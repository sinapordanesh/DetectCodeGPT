def solve(H, W, T):
    MOD = 10**9 + 7
    if H * W % T != 0:
        return 0
    T = pow(2, T, MOD - 1)
    res = pow(3, H * W // T, MOD) - 2 * pow(2, H * W // T, MOD) + pow(2, H * W // T, MOD)
    return res % MOD

# Sample Input 1
print(solve(2, 2, 1))

# Sample Input 2
print(solve(869, 120, 1001))