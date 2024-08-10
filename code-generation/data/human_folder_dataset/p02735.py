
def resolve():
    INF = 1 << 60
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]

    # 長方形区域を選んで、その中の通路と壁を反転する操作ができる
    # dp[ y ][ x ] := マス (y, x) に到達するまでに魔法を唱える回数の最小値

    dp = [[INF] * W for _ in range(H)]
    if G[0][0] == "#":
        dp[0][0] = 1
    else:
        dp[0][0] = 0

    # 1, (nx, ny) が通路のとき, 操作なし
    # 2, (nx, ny) か壁で、(x, y) が通路のとき, 操作する
    # 3, (nx, ny) が壁で、(x, y) も壁のとき, 2の操作が継続中

    drc = [(0, 1), (1, 0)]
    for y in range(H):
        for x in range(W):
            for dy, dx in drc:
                ny = y + dy
                nx = x + dx
                if ny >= H or nx >= W:
                    continue
                cost = 0
                if G[ny][nx] == "#" and G[y][x] == ".":
                    cost = 1
                dp[ny][nx] = min(dp[ny][nx], dp[y][x] + cost)

    print(dp[H - 1][W - 1])


if __name__ == "__main__":
    resolve()