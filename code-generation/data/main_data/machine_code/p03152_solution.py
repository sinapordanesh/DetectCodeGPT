import numpy as np

def fun(N, M, A, B):
    mod = 10**9 + 7
    dp = np.zeros((N+1, M+1), dtype=int)
    dp[0][0] = 1
    
    for i in range(N+1):
        for j in range(M+1):
            if i > 0 and j > 0:
                dp[i][j] += (A[i-1] == B[j-1]) * dp[i-1][j-1]
            if i > 0:
                dp[i][j] += (A[i-1] >= B[j]) * dp[i-1][j]
            if j > 0:
                dp[i][j] += (A[i] >= B[j-1]) * dp[i][j-1]
            dp[i][j] %= mod
    
    return dp[N][M]

# Sample Input 1
print(fun(2, 2, [4, 3], [3, 4]))

# Sample Input 2
print(fun(3, 3, [5, 9, 7], [3, 6, 9]))

# Sample Input 3
print(fun(2, 2, [4, 4], [4, 4]))

# Sample Input 4
print(fun(14, 13, [158, 167, 181, 147, 178, 151, 179, 182, 176, 169, 180, 129, 175, 168], [181, 150, 178, 179, 167, 180, 176, 169, 182, 177, 175, 159, 173]))