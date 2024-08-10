def solve():
    H, W = map(int, input().split())
    c = []
    for _ in range(H):
        c.append(list(map(int, input().split())))

    dp = [[0] * W for _ in range(H)]

    for x in range(H):
        dp[x][0] = 1 if c[x][0] == 0 else 0
    for y in range(W):
        dp[0][y] = 1 if c[0][y] == 0 else 0

    for x in range(H-1):
        for y in range(W-1):
            if c[x+1][y+1] == 0:
                dp[x+1][y+1] = min([dp[x][y], dp[x][y+1], dp[x+1][y]]) + 1

    print(max([max(item) for item in dp])**2)


if __name__ == '__main__':
    solve()