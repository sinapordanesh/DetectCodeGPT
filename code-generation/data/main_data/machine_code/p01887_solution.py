def min_time_cost(W, H, K, N, dogs):
    if W % 2 == 0 or H % 2 == 0:
        return -1

    dog_blocks = set()
    for dog in dogs:
        dog_blocks.add(dog)

    dp = [[[float('inf')] * (K + 1) for _ in range(W)] for _ in range(H)]
    dp[0][0][0] = 0

    for k in range(K + 1):
        for i in range(H):
            for j in range(W):
                if dp[i][j][k] == float('inf'):
                    continue

                if i + 2 < H and j - 1 >= 0:
                    if (j - 1, i + 2) in dog_blocks:
                        if k + 2 <= K:
                            dp[i + 2][j - 1][k + 2] = min(dp[i + 2][j - 1][k + 2], dp[i][j][k] + 2)
                    else:
                        dp[i + 2][j - 1][k] = min(dp[i + 2][j - 1][k], dp[i][j][k] + 1)

                if i + 2 < H and j + 1 < W:
                    if (j + 1, i + 2) in dog_blocks:
                        if k + 2 <= K:
                            dp[i + 2][j + 1][k + 2] = min(dp[i + 2][j + 1][k + 2], dp[i][j][k] + 2)
                    else:
                        dp[i + 2][j + 1][k] = min(dp[i + 2][j + 1][k], dp[i][j][k] + 1)

                if i + 2 < H and j + 2 < W:
                    if (j + 2, i + 2) in dog_blocks:
                        if k + 2 <= K:
                            dp[i + 2][j + 2][k + 2] = min(dp[i + 2][j + 2][k + 2], dp[i][j][k] + 2)
                    else:
                        dp[i + 2][j + 2][k] = min(dp[i + 2][j + 2][k], dp[i][j][k] + 1)

    ans = min(dp[-1][-1])
    return ans if ans != float('inf') else -1