import sys
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

N = ii()
S = input()
'''
cnt = [0]*(N+1)
ans = N+1

for i in range(N):
    if S[i] == '.':
        cnt[i+1] += cnt[i] + 1
    else:
        cnt[i+1] += cnt[i]

for i in range(0, N+1):
    ans = min(ans, (i-cnt[i])+(cnt[N]-cnt[i]))

print(ans)
'''

dp = dp2(0, 2, N+1)

if S[0] == '.':
    dp[1][0] = 0
    dp[1][1] = 1
else:
    dp[1][0] = 1
    dp[1][1] = 0

for i in range(2, N+1):
    for j in range(2):
        if S[i-1] == '.':
            dp[i][0] = dp[i-1][0]
            dp[i][1] = min(dp[i-1][0]+1, dp[i-1][1]+1)
        else:
            dp[i][0] = dp[i-1][0] + 1
            dp[i][1] = min(dp[i-1][0], dp[i-1][1])

print(min(dp[N][0], dp[N][1]))