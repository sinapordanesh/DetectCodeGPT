def lowest_budget_cost(n, m, k, proposals):
    import sys

    INF = sys.maxsize
    dp = [[[INF] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 0

    for i in range(1, m + 1):
        u, v, w, l = proposals[i - 1]
        for x in range(n + 1):
            for y in range(n + 1):
                for z in range(n + 1):
                    if dp[x][y][z] != INF:
                        if l == "A":
                            if x < k:
                                dp[x + 1][y][z] = min(dp[x + 1][y][z], dp[x][y][z] + w)
                            else:
                                dp[x][y][z] = min(dp[x][y][z], dp[x][y][z] + w)
                        else:
                            if y < n - 1 - k:
                                dp[x][y + 1][z] = min(dp[x][y + 1][z], dp[x][y][z] + w)
                            else:
                                dp[x][y][z] = min(dp[x][y][z], dp[x][y][z] + w)

    ans = INF
    for x in range(n + 1):
        for y in range(n + 1):
            ans = min(ans, dp[x][y][n - 1 - k])

    if ans == INF:
        return -1
    return ans

# Sample Input
print(lowest_budget_cost(4, 5, 2, [(1, 2, 2, 'A'), (1, 3, 2, 'A'), (1, 4, 2, 'A'), (2, 3, 1, 'B'), (3, 4, 1, 'B')]))
print(lowest_budget_cost(5, 8, 2, [(1, 2, 1, 'A'), (2, 3, 1, 'A'), (3, 4, 3, 'A'), (4, 5, 3, 'A'), (1, 2, 5, 'B'), (2, 3, 5, 'B'), (3, 4, 8, 'B'), (4, 5, 8, 'B')]))
print(lowest_budget_cost(5, 5, 1, [(1, 2, 1, 'A'), (2, 3, 1, 'A'), (3, 4, 1, 'A'), (4, 5, 1, 'B'), (3, 5, 1, 'B')]))
print(lowest_budget_cost(4, 5, 3, [(1, 2, 2, 'A'), (2, 4, 3, 'B'), (3, 4, 4, 'B'), (2, 3, 5, 'A'), (3, 1, 6, 'A')]))