from collections import Counter
from itertools import permutations
import sys
readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    N = int(readline())
    if N == 0:
        return False
    def dist(a, b):
        LA = len(a); LB = len(b)
        dp = [[10**18]*(LB+1) for i in range(LA+1)]
        dp[0][0] = 0
        for i in range(LA):
            for j in range(LB):
                v = dp[i][j]
                if a[i] == b[j]:
                    dp[i+1][j+1] = min(dp[i+1][j+1], v)
                else:
                    dp[i+1][j+1] = min(dp[i+1][j+1], v+1)
                dp[i+1][j] = min(dp[i+1][j], v+1)
                dp[i][j+1] = min(dp[i][j+1], v+1)
            dp[i+1][LB] = min(dp[i+1][LB], dp[i][LB]+1)
        for j in range(LB):
            dp[LA][j+1] = min(dp[LA][j+1], dp[LA][j] + 1)
        return dp[LA][LB]
    def check(a, b):
        LA = len(a); LB = len(b)
        if abs(LA - LB) > D:
            return False
        d = dist(a, b)
        if d <= D:
            return True
        if d == 2 and LA == LB:
            ra = []; rb = []; rp = []
            for i in range(LA):
                if a[i] != b[i]:
                    rp.append(i)
                    ra.append(a[i])
                    rb.append(b[i])
            if len(rp) == 2 and rp[1] - rp[0] == 1:
                ra.reverse()
                if ra == rb:
                    return True
        if D == 2:
            if d == 4 and LA == LB:
                ra = []; rb = []; rp = []
                for i in range(LA):
                    if a[i] != b[i]:
                        rp.append(i)
                        ra.append(a[i])
                        rb.append(b[i])
                if len(rp) == 4 and rp[1] - rp[0] == 1 and rp[3] - rp[2] == 1:
                    ra[0], ra[1] = ra[1], ra[0]
                    ra[2], ra[3] = ra[3], ra[2]
                    return ra == rb
            if d == 3 and abs(LA - LB) < D:
                a = list(a); b = list(b)
                if not LA < LB:
                    LA, LB = LB, LA
                    a, b = b, a
                for i in range(LA-1):
                    a[i], a[i+1] = a[i+1], a[i]
                    if dist(a, b) <= D-1:
                        return True
                    for j in range(LA-1):
                        a[j], a[j+1] = a[j+1], a[j]
                        if a == b:
                            return True
                        a[j], a[j+1] = a[j+1], a[j]
                    a[i], a[i+1] = a[i+1], a[i]
        return False
    D = int(readline())
    S = [readline().strip() for i in range(N)]
    ans = []
    for i in range(N):
        for j in range(i+1, N):
            if check(S[i], S[j]):
                ans.append((S[i], S[j]) if S[i] < S[j] else (S[j], S[i]))
    ans.sort()
    for e in ans:
        write("%s,%s\n" % e)
    write("%d\n" % len(ans))
    return True
while solve():
    ...
