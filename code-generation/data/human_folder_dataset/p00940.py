import sys
readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    P, R, T = map(int, readline().split())
    *L, = map(int, readline().split())
    RS = [list(map(int, readline().split())) for i in range(P)]
    LG = [list(map(int, input().split())) for i in range(T)]

    prv = -1
    K = [[0]*R for i in range(P)]
    def check(t):
        nonlocal prv
        if prv < t:
            for i in range(prv+1, t+1):
                p, r = LG[i]
                K[p-1][r-1] += 1
                L[r-1] -= 1
        else:
            for i in range(t+1, prv+1):
                p, r = LG[i]
                K[p-1][r-1] -= 1
                L[r-1] += 1
        S = L[:]; U = [0]*P
        updated = 1
        while updated:
            updated = 0
            for i in range(P):
                if U[i]:
                    continue
                for j in range(R):
                    if RS[i][j] - K[i][j] > max(S[j], 0):
                        break
                else:
                    U[i] = 1
                    for j in range(R):
                        S[j] += K[i][j]
                    updated = 1
        prv = t
        return sum(U) == P

    left = 0; right = T
    while left+1 < right:
        mid = (left + right) >> 1
        if check(mid):
            left = mid
        else:
            right = mid
    if right == T:
        write("-1\n")
    else:
        write("%d\n" % (right+1))
solve()
