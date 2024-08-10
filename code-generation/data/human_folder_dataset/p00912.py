import sys
readline = sys.stdin.readline
write = sys.stdout.write
def check(W, N, k, su, s):
    vs = [0]*(N+2)
    vs[1] = r = 1
    p = q = 0
    for i in range(N):
        while (su[i+1] - su[p]) + (i - p)*s >= W:
            p += 1
        while (su[i+1] - su[q]) + (i - q) > W:
            q += 1
        vs[i+2] = r = r + (vs[p] > vs[q])
        if r == vs[q]:
            return k < i+2 and r - vs[k]
    return vs[N+1] - vs[k]
def solve():
    W, N = map(int, readline().split())
    if W == N == 0:
        return False
    *X, = map(int, readline().split())
    su = [0]*(N+1)
    for i in range(N):
        su[i+1] = su[i] + X[i]
    k = N
    while k > 0 and su[N] - su[k-1] + (N-k+1) <= W:
        k -= 1

    ma = 0
    cu = X[0]; c = 1
    for i in range(1, N):
        if cu + c + X[i] > W:
            ma = max(ma, (W - cu + c-2) // (c-1))
            cu = X[i]
            c = 1
        else:
            cu += X[i]
            c += 1

    left = 0; right = ma+1
    while left+1 < right:
        mid = (left + right) >> 1
        if check(W, N, k, su, mid):
            right = mid
        else:
            left = mid
    write("%d\n" % right)
    return True
while solve():
    ...
