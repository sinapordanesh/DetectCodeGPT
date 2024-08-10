def original_value(N, X):
    MOD = 998244353
    ans = 0
    for k in range(X+1):
        count = 0
        original_k = k
        while k != original_k or count == 0:
            if k % 2 == 1:
                k = (k - 1) // 2
            else:
                k = k // 2 + 2 ** (N - 1)
            count += 1
        ans += count
    return ans % MOD

N, X = map(int, input().split())
print(original_value(N, X))