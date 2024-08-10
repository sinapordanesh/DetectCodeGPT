import sys
readline = sys.stdin.readline
write = sys.stdout.write
def check(N, A, B, S):
    K = min(A, B)
    g = 0
    for s in S:
        g ^= s % (K+1)

    if A == B:
        return g != 0
    if A > B:
        if g != 0:
            return 1
        for s in S:
            if s > B:
                return 1
        return 0

    cnt = 0; m = 1
    r = 0
    for s in S:
        if s > A:
            cnt += 1
            r = s
            g0 = g ^ (s % (K+1))
    if cnt > 1:
        return 0
    if cnt == 0:
        return g != 0
    return g0 <= A and 1 <= r - g0 <= A

def solve():
    N, A, B = map(int, readline().split())
    S = [int(readline()) for i in range(N)]
    if check(N, A, B, S):
        write("Hanako\n")
    else:
        write("Jiro\n")
solve()
