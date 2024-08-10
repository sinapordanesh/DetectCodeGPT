MOD = 10**9 + 7

def count_ways_to_paint_arcs(N, M, S):
    if N == 1:
        return 1
    
    dp = [0] * (M+1)
    dp[0] = dp[1] = 1
    
    for i in range(2, M+1):
        dp[i] = (dp[i-1] + dp[i-2]) % MOD
    
    for i in range(1, M):
        if S[i] == S[i-1]:
            return 0
    
    if S[0] == S[-1]:
        ans = dp[N]
    else:
        ans = dp[N] * 2 % MOD
    
    return ans

# Sample Input 1
N = 4
M = 7
S = "RBRRBRR"
print(count_ways_to_paint_arcs(N, M, S))

# Sample Input 2
N = 3
M = 3
S = "BBB"
print(count_ways_to_paint_arcs(N, M, S))

# Sample Input 3
N = 12
M = 10
S = "RRRRBRRRRB"
print(count_ways_to_paint_arcs(N, M, S))