def edu_dp_d_matching():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    dp = [[0] * (1 << n) for _ in range(n)]
    for i in range(n):
        if a[0][i] == 1: dp[0][(1 << i)] = 1
    for i in range(1, n):
        for k in range(1 << n):
            if dp[i - 1][k] == 0: continue
            for j in range(n):
                if a[i][j] == 0 or k & (1 << j) != 0: continue
                dp[i][k | (1 << j)] += dp[i - 1][k]

    print(dp[-1][-1] % (pow(10, 9) + 7))


edu_dp_d_matching()