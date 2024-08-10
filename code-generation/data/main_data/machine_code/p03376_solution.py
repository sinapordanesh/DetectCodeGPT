def max_doughnuts(N, X, D, doughnuts):
    dp = [0] * (X+1)
    dp[0] = 0
    for i in range(1, X+1):
        for j in range(N):
            if i >= doughnuts[j][1]:
                dp[i] = max(dp[i], dp[i - doughnuts[j][1]] + 1)
            else:
                break
    return dp[X]

N, X, D = map(int, input().split())
doughnuts = []
for _ in range(N):
    m, p = map(int, input().split())
    doughnuts.append((m, p))

print(max_doughnuts(N, X, D, doughnuts))