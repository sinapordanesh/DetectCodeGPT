import sys
readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    N = int(readline())
    W = [(0, 50)]
    for i in range(N):
        b, h = map(int, readline().split())
        W.append((b, h))
    W.append((100, 50))
    M = int(readline())
    S = [0]*(N+1)
    Q = []
    for i in range(M):
        f, a = map(int, readline().split())
        for j in range(N+1):
            if W[j][0] < f < W[j+1][0]:
                S[j] += a
                break
    L = int(readline())
    for i in range(L):
        p, t = map(int, readline().split())
        Q.append((t, i, p))
    Q.sort(reverse=1)
    T = [0]*(N+1)
    C = N+1
    tc = 0
    ans = [50] * L
    EPS = 1e-9
    while 1:
        k = -1; tm = 10**18
        for i in range(C):
            if S[i] == 0:
                continue
            b0, h0 = W[i]; b1, h1 = W[i+1]
            t = (min(h0, h1) * (b1 - b0) * 30 - T[i]) / S[i]
            if t < tm:
                tm = t
                k = i
        assert k != -1
        b0, h0 = W[k]; b1, h1 = W[k+1]
        dt = (min(h0, h1) * (b1 - b0) * 30 - T[k]) / S[k]
        while Q and tc <= Q[-1][0] < tc + dt:
            t, i, p = Q.pop()
            for j in range(C):
                ba, ha = W[j]; bb, hb = W[j+1]
                if ba < p < bb:
                    dt0 = t - tc
                    ans[i] = (S[j] * dt0 + T[j]) / ((bb - ba) * 30)
                    break
        for i in range(C):
            T[i] += S[i] * dt
        if C == 1:
            break
        if h0 < h1:
            if abs(T[k-1] - h0 * (b0 - W[k-1][0]) * 30) < EPS:
                assert S[k-1] == 0
                S[k-1] = S[k]
                T[k-1] += T[k]
                S.pop(k); T.pop(k); W.pop(k)
                C -= 1
            else:
                j = k-1
                while T[j] == W[j][1]:
                    j -= 1
                S[j] += S[k]
                S[k] = 0
        else:
            if abs(T[k+1] - h1 * (W[k+2][0] - b1) * 30) < EPS:
                assert S[k+1] == 0
                S[k+1] = S[k]
                T[k+1] += T[k]
                S.pop(k); T.pop(k); W.pop(k+1)
                C -= 1
            else:
                j = k+1
                while T[j] == W[j+1][1]:
                    j += 1
                S[j] += S[k]
                S[k] = 0
        tc += dt
    for i in range(L):
        write("%.16f\n" % ans[i])
D = int(readline())
for i in range(D):
    solve()
