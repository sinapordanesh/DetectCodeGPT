import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
a = list(map(int, input().split()))
def sub(a, minus=False):
    m = 20
    inf = 10**15
    dp = [[inf]*m for _ in range(n)] # i以降、a[i]に4^jをかけたところからソート
    for j in range(m):
        dp[-1][j] = j
    for i in range(n-2, -1, -1):
        if a[i]>a[i+1]:
            v = 0
            ai = a[i]; ai1 = a[i+1]
            while ai>ai1:
                ai1 *= 4
                v += 1
            for j in range(m):
                if j+v<m:
                    dp[i][j] = j + dp[i+1][j+v]
                else:
                    dp[i][j] = j + dp[i+1][m-1] + (n-i-1)*(j+v-m+1)
        else:
            v = 0
            ai = a[i]; ai1 = a[i+1]
            while True:
                ai *= 4
                if ai<=ai1:
                    v += 1
                else:
                    break
            for j in range(m):
                dp[i][j] = j + dp[i+1][max(0, j-v)]
    if minus:
        ans = [(2*min(dp[i][j] for j in range(m))+(n-i)) for i in range(n)]
    else:
        ans = [2*min(dp[i][j] for j in range(m)) for i in range(n)]
    return ans
dp0 = sub(list(a))
dp1 = sub([item for item in a[::-1]], minus=True)[::-1]
dp0.append(0)
dp1.insert(0,0)
ans = min((dp0[i]+dp1[i]) for i in range(n+1))
print(ans)