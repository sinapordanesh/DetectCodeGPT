import sys

sys.setrecursionlimit(10**6)
int1 = lambda x: int(x)-1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

n = II()
aa = LI1()
dp = [[-10]*n for _ in range(n)]
mx = [-10]*(n+1)
nmx = [-10]*(n+1)
a, b = min(aa[:2]), max(aa[:2])
dp[a][b] = dp[b][a] = 0
mx[a] = mx[b] = mx[n] = 0

def chmax(i, j, val):
    if val < 0: return
    if val > dp[i][j]:
        dp[i][j] = dp[j][i] = val
        nmx[i] = max(nmx[i], val)
        nmx[j] = max(nmx[j], val)
        nmx[n] = max(nmx[n], val)

base = 0
for i in range(n-1):
    abc = aa[i*3+2:i*3+5]
    # print(abc)
    abc.sort()
    a, b, c = abc
    # 3枚とも同じ場合
    if a == c:
        base += 1
        continue
    # b==cのときa==bになるようにする
    if b == c: a, c = c, a
    # ペアがある場合
    if a == b:
        vc = dp[c][c]
        for x, v in enumerate(dp[a][:]): chmax(c, x, v+1)
        chmax(a, c, max(mx[n], dp[a][a]+1))
        chmax(a, a, max(mx[n], vc+1))
        for x in range(n): chmax(a, x, mx[x])
        for x in range(n): chmax(c, x, mx[x])
    # 3枚とも異なる場合
    else:
        # a,b,cから2枚残す場合
        chmax(b, c, max(dp[a][a]+1, mx[n]))
        chmax(a, c, max(dp[b][b]+1, mx[n]))
        chmax(a, b, max(dp[c][c]+1, mx[n]))
        # a,b,cから1枚残す場合
        for x in range(n):
            chmax(a, x, mx[x])
            chmax(b, x, mx[x])
            chmax(c, x, mx[x])

    for x in range(n+1): mx[x] = max(mx[x], nmx[x])
    # p2D(dp)
    # print(mx)
    # print()

a = aa[-1]
ans = max(mx[n], dp[a][a]+1)+base
print(ans)
