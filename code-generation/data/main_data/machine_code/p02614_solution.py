def count_choices(H, W, K, grid):
    ans = 0
    for i in range(1 << H):
        for j in range(1 << W):
            cnt = 0
            for x in range(H):
                for y in range(W):
                    if (i >> x) & 1 == 0 and (j >> y) & 1 == 0 and grid[x][y] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    return ans

# Input
H, W, K = map(int, input().split())
grid = [input() for _ in range(H)]

# Output
print(count_choices(H, W, K, grid))