def main():
    n = int(input())
    grid = [input() for _ in [0]*n]
    for i in grid:
        if "#" in i:
            break
    else:
        print(-1)
        return
    ans = 10**20
    # i行目に何個黒があるか
    black_cnt = [0]*n
    # i列目に黒が一つでもあればTrue
    exist = [False]*n
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "#":
                black_cnt[i] += 1
                exist[j] = True
    # 縦一列が既に黒の列の数
    all_cnt = 0
    for j in range(n):
        for i in range(n):
            if grid[i][j] == ".":
                break
        else:
            all_cnt += 1
    for i in range(n):
        if exist[i]:
            ans = min(ans, n-black_cnt[i]+n-all_cnt)
        else:
            ans = min(ans, 2*n-black_cnt[i]-all_cnt+1)
    print(ans)


main()
