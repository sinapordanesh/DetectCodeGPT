def solve_tournament(N, M, A):
    mod = 10**9 + 7
    dp = [0] * (1 << N)
    dp[0] = 1
    
    for i in range(1 << N):
        bits = bin(i).count('1')
        for j in range(M):
            loser = A[j] - 1
            if dp[i & ~(1 << loser)] != 0 and (loser >= N or (i & (1 << loser)) != 0):
                dp[i] += dp[i & ~(1 << loser)]
                dp[i] %= mod
    
    return dp[(1 << N) - 1]

# Input
N, M = map(int, input().split())
A = list(map(int, input().split()))

# Output
print(solve_tournament(N, M, A))