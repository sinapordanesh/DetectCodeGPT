def main():
    n = int(input())
    ab = [sorted(list(map(int, input().split()))) for _ in [0]*(n-1)]
    s = list(map(int, input().split()))

    g = [[] for _ in [0]*n]
    [g[a-1].append(b-1) for a, b in ab]
    [g[b-1].append(a-1) for a, b in ab]
    root = 0  # 根
    d = [-1]*n  # 根からの距離
    d[root] = 0
    q = [root]
    cnt = 0
    while q:  # BFS
        cnt += 1
        qq = []
        while q:
            i = q.pop()
            for j in g[i]:
                if d[j] == -1:
                    d[j] = cnt
                    qq.append(j)
        q = qq

    dd = [[j, i] for i, j in enumerate(d)]
    dd.sort(key=lambda x: -x[0])
    dd = [j for i, j in dd]

    dp = [1]*n
    for i in dd:
        for j in g[i]:
            if d[j] > d[i]:
                dp[i] += dp[j]

    ans = []
    for a, b in ab:
        a -= 1
        b -= 1
        if d[a] > d[b]:
            a, b = b, a
        ay = dp[b]-1
        ax = n-2-ay
        if ax-ay == 0:
            ans.append(1j)
        else:
            ans.append(abs(s[a]-s[b])//abs(ax-ay))

    ab_dict = {(ab[i][0]-1, ab[i][1]-1): ans[i] for i in range(n-1)}

    if 1j in ans:
        cnt = 0
        for i in ans:
            if i == 1j:
                cnt += 1
        if cnt > 1:
            return
        p = ans.index(1j)
        q = [root]

        temp_1 = 0
        temp_2 = 0
        while q:
            qq = []
            while q:
                i = q.pop()
                for j in g[i]:
                    if d[j] > d[i]:
                        a, b = min(i, j), max(i, j)
                        temp = ab_dict[(a, b)]
                        if temp == 1j:
                            temp_2 = dp[j]
                        else:
                            temp_1 += dp[j]*temp
                        qq.append(j)
            q = qq

        ans[p] = (s[0]-temp_1)//temp_2

    for i in ans:
        print(i)


main()
