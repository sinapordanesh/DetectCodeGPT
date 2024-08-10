mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    H, W, d = map(int, input().split())

    N = 1500
    grid = [[""] * N for _ in range(N)]
    if d & 1:
        ans = [[""] * W for _ in range(H)]
        for h in range(H):
            for w in range(W):
                if (h+w) & 1:
                    ans[h][w] = "R"
                else:
                    ans[h][w] = "B"
        for h in range(H):
            print("".join(ans[h]))
        exit()

    grid = [[""] * N for _ in range(N)]
    e = (d-2) // 2
    for h in range(N):
        if h * d >= N:
            break
        for w in range(N):
            if w * d >= N:
                break
            if (h+w) & 1:
                c = "R"
            else:
                c = "B"
            for hh in range(h*d - e, h*d + e + 1):
                for ww in range(w*d - e, w*d + e + 1):
                    if 0 <= hh < N and 0 <= ww < N and abs(h*d-hh) + abs(w*d-ww) <= e:
                        grid[hh][ww] = c
    for h in range(N):
        if h * d + d//2 >= N:
            break
        for w in range(N):
            if w * d + d//2 >= N:
                break
            if (h+w) & 1:
                c = "Y"
            else:
                c = "G"
            for hh in range(h*d + d//2 - e, h*d + d//2 + e + 1):
                for ww in range(w*d + d//2 - e, w*d + d//2 + e + 1):
                    if 0 <= hh < N and 0 <= ww < N and abs(h*d + d//2 - hh) + abs(w*d + d//2 - ww) <= e:
                        grid[hh][ww] = c

    for h in range(1, N):
        for w in range(N):
            if grid[h][w] == "":
                grid[h][w] = grid[h-1][w]

    for h in range(501, 500+H+1):
        print("".join(grid[h][501:500+W+1]))


if __name__ == '__main__':
    main()
