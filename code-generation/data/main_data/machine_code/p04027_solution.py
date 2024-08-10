def activity_level(N, C, A, B):
    MOD = 10**9 + 7
    dp = [0] * (C+1)
    dp[0] = 1
    
    for i in range(1, N+1):
        for j in range(C, -1, -1):
            for k in range(A[i-1], B[i-1]+1):
                if j - k < 0:
                    break
                dp[j] += dp[j-k]
                dp[j] %= MOD
    
    return dp[C]

N, C = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(activity_level(N, C, A, B))