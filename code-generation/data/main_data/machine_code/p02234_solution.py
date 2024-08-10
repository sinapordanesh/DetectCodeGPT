def matrix_chain_multiplication(arr):
    n = len(arr)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for length in range(2, n):
        for i in range(1, n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + arr[i-1] * arr[k] * arr[j])
    return dp[1][n-1]

n = int(input())
arr = []
for _ in range(n):
    r, c = map(int, input().split())
    arr.append(r)
arr.append(c)
print(matrix_chain_multiplication(arr))