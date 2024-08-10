def f(r, c):
    dp = [[0]*(c+1) for _ in range(r+1)]
    dp[0][0] = 1
    for i in range(r+1):
        for j in range(c+1):
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
            dp[i][j] %= (10**9 + 7)
    return dp[r][c]

def sum_f(r1, c1, r2, c2):
    total = 0
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            total += f(i, j)
            total %= (10**9 + 7)
    return total

r1, c1, r2, c2 = map(int, input().split())
print(sum_f(r1, c1, r2, c2))