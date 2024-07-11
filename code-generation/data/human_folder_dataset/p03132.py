import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


l = int(input())
a = [None]*l
for i in range(l):
    a[i] = int(input())
dp = [[float("inf")]*(l+1) for _ in range(5)]
for i in range(5):
    dp[i][0] = 0
def c1(v):
    if v==0:
        return 2
    else:
        return v%2
def c2(v):
    if v%2==0:
        return 1
    else:
        return 0
for i in range(1,l+1):
    v = a[i-1]
    m = dp[0][i-1]
    dp[0][i] = m + v
    m = min(m, dp[1][i-1])
    dp[1][i] = m + c1(v)
    m = min(m, dp[2][i-1])
    dp[2][i] = m + c2(v)
    m = min(m, dp[3][i-1])
    dp[3][i] = m + c1(v)
    m = min(m, dp[4][i-1])
    dp[4][i] = m + v
ans = min(dp[i][l] for i in range(5))
print(ans)