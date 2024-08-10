n = int(input())
xyp = [list(map(int,input().split())) for i in range(n)]

def caldp(a):
    n = len(a)
    a.sort()
    dp = [[float("INF")]*(n+1) for i in range(n+1)]
    dp[0][0] = 0
    for l in range(n):
        for r in range(l+1,n+1):
            now = float("INF")
            for k in range(l,r):
                count = 0
                for i in range(l,r):
                    count += abs(a[i][0]-a[k][0])*a[i][1]
                    if count >= now:
                        break
                now = min(now,count)
            for j in range(n):
                dp[r][j+1] = min(dp[r][j+1],dp[l][j]+now)

            now = 0
            for i in range(l,r):
                now += abs(a[i][0])*a[i][1]
            for j in range(n+1):
                dp[r][j] = min(dp[r][j],dp[l][j]+now)

    res = [float("INF")]*(n+1)
    for i in range(n+1):
        res[i] = dp[-1][i]
    return res

ans = [float("INF")]*(n+1)

for s in range(1<<n):
    lx = []
    ly = []
    for i in range(n):
        if s >> i & 1:
            lx.append((xyp[i][0],xyp[i][2]))
        else:
            ly.append((xyp[i][1],xyp[i][2]))
    lx = caldp(lx)
    ly = caldp(ly)
    for i in range(len(lx)):
        for j in range(len(ly)):
            ans[i+j] = min(ans[i+j],lx[i]+ly[j])

for i in ans:
    print(i)