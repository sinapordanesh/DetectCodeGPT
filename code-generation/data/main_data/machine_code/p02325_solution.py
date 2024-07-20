import math

def bitonic_tsp_distance(N, points):
    def dist(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    dp = [[float('inf')] * N for _ in range(N)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(i):
            for k in range(j+1, i):
                dp[j][i] = min(dp[j][i], dp[j][k] + dist(points[k], points[i]))

        for j in range(i):
            dp[j][i] = min(dp[j][i], dp[j][i-1] + dist(points[i-1], points[i]))

    result = float('inf')
    for i in range(N):
        result = min(result, dp[i][N-1] + dist(points[i], points[N-1]))

    return round(result, 8)