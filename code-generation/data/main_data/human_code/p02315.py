def main():
    N, W = map(int, input().split())
    value = []
    weight = []
    for i in range(N):
        a, b = map(int, input().split())
        value.append(a)
        weight.append(b)
    dp = [[-float("inf") for i in range(W+1)] for j in range(N+1)]
    for w in range(W+1):
        dp[0][w] = 0

    for i in range(N):
        for w in range(W+1):
            if w >= weight[i]:
                dp[i+1][w] = max(dp[i][w-weight[i]]+value[i], dp[i][w])
            else:
                dp[i+1][w] = dp[i][w]
    return dp[N][W]

if __name__ == '__main__':
    print(main())

