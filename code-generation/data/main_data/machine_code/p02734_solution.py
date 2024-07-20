def f(N, S, A):
    mod = 998244353
    dp = [[0] * (N+1) for _ in range(N+1)]
    for l in range(1, N+1):
        for r in range(l, N+1):
            if l == r:
                dp[l][r] = 1 if A[l-1] == S else 0
            else:
                dp[l][r] = (dp[l][r-1] + dp[l-1][r-1]) % mod
                if sum(A[l-1:r]) == S:
                    dp[l][r] += 1
    return sum(sum(row) for row in dp) % mod

# Input
N, S = map(int, input().split())
A = list(map(int, input().split()))

# Output
print(f(N, S, A))