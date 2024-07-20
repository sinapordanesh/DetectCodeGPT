import sys
readline = sys.stdin.readline
write = sys.stdout.write
def check(N, C, T, x):
    used = [0]*N
    S = [0]*(T+1)
    cap = x
    f = 0
    for t in range(T):
        cap += S[t]
        if cap == 0:
            continue
        for i in range(f, N):
            if used[i]:
                continue
            m, l, k = C[i]
            if t+m > T:
                break
            if t % (l + k) <= l:
                used[i] = 1
                S[t+m] += 1
                cap -= 1
                if i == f:
                    while f < N and used[f]:
                        f += 1
                if cap == 0:
                    break
    cap += S[T]
    return sum(used) == N and cap == x

def solve():
    N, T = map(int, readline().split())
    if N == 0:
        return False
    C = [list(map(int, readline().split())) for i in range(N)]
    for x in range(N+1):
        if check(N, C, T, x):
            write("%d\n" % x)
            break
    return True
while solve():
    ...
