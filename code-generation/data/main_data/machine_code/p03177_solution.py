def count_directed_paths(N, K, edges):
    MOD = 10**9 + 7
    
    def matmul(A, B):
        C = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    C[i][j] = (C[i][j] + A[i][k]*B[k][j]) % MOD
        return C
    
    dp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dp[i][j] = edges[i][j]
    
    res = [[0]*N for _ in range(N)]
    for i in range(N):
        res[i][i] = 1
    
    while K > 0:
        if K % 2 == 1:
            res = matmul(res, dp)
        dp = matmul(dp, dp)
        K //= 2
    
    count = sum(sum(row) for row in res) % MOD
    return count

# Read input
N, K = map(int, input().split())
edges = []
for _ in range(N):
    edges.append(list(map(int, input().split())))

# Call the function and print the output
print(count_directed_paths(N, K, edges))