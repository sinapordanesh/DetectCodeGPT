def main():
    N, W = map(int, input().split())
    weight = [0] * N
    value = [0] * N
    for i in range(N):
        weight[i], value[i] = map(int, input().split())
    V = sum(value)
    dp = [[float('inf')] * (V + 5) for _ in range(N + 5)]
    dp[0][0] = 0
    for i in range(N):
        for v in range(V+1):
            if v - value[i] >= 0:
                dp[i+1][v] = min(dp[i][v-value[i]] + weight[i], dp[i][v])
            else:
                dp[i+1][v] = dp[i][v]
    ans = 0
    for v in range(V+1):
        if dp[N][v] <= W:
            ans = v
    print(ans)

if __name__ == "__main__":
    main()