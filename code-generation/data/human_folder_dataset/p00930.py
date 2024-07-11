from heapq import heappush, heappop, heapify
import sys
readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    N, Q = map(int, readline().split())

    INF = 2**31-1

    LV = (N-1).bit_length()
    N0 = 2**LV
    data = [0]*(2*N0)
    lazy = [0]*(2*N0)
    L0 = [0]*(2*N0)
    L1 = [0]*(2*N0)

    def init(A):
        for i in range(N):
            data[N0-1+i] = A[i]
        for i in range(N0):
            L0[N0-1+i] = L1[N0-1+i] = i
        for i in range(N0-2, -1, -1):
            data[i] = min(data[2*i+1], data[2*i+2])
            L0[i] = L0[2*i+1]
            L1[i] = L1[2*i+2]

    def gindex(l, r):
        L = (l + N0) >> 1; R = (r + N0) >> 1
        lc = 0 if l & 1 else (L & -L).bit_length()
        rc = 0 if r & 1 else (R & -R).bit_length()
        for i in range(LV):
            if rc <= i:
                yield R
            if L < R and lc <= i:
                yield L
            L >>= 1; R >>= 1

    def propagates(*ids):
        for i in reversed(ids):
            v = lazy[i-1]
            if not v:
                continue
            lazy[2*i-1] += v; lazy[2*i] += v
            data[2*i-1] += v; data[2*i] += v
            lazy[i-1] = 0

    def update(l, r, x):
        *ids, = gindex(l, r)
        propagates(*ids)

        L = N0 + l; R = N0 + r
        while L < R:
            if R & 1:
                R -= 1
                lazy[R-1] += x; data[R-1] += x
            if L & 1:
                lazy[L-1] += x; data[L-1] += x
                L += 1
            L >>= 1; R >>= 1
        for i in ids:
            data[i-1] = min(data[2*i-1], data[2*i])
        u = 1

    def query(r):
        propagates(*gindex(0, r))
        R = N0 + r

        R = N0 + r
        while R:
            if R & 1:
                R -= 1
                if data[R-1] < 2:
                    l0 = L0[R-1]
                    r0 = L1[R-1]+1
                    break
            R >>= 1
        else:
            return 0

        k = R-1
        while k < N0-1:
            v = lazy[k]
            if v:
                lazy[2*k+1] += v; lazy[2*k+2] += v
                data[2*k+1] += v; data[2*k+2] += v
                lazy[k] = 0
            if data[2*k+2] < 2:
                l0 = (l0 + r0) >> 1
                k = 2*k+2
            else:
                r0 = (l0 + r0) >> 1
                k = 2*k+1
        return r0

    que = []
    *s, = map("()".index, readline().strip())
    A = [0]*N
    C = [0]*N
    cur = 0
    for i in range(N):
        if s[i]:
            que.append(i)
            C[i] = 1
            cur -= 1
        else:
            cur += 1
        A[i] = cur
    heapify(que)
    init(A)

    for i in range(Q):
        q = int(readline())
        if s[q-1] == 0:
            while que and s[que[0]] == 0:
                v = heappop(que)
                C[v] = 0
            if not que or q-1 <= que[0]:
                write("%d\n" % q)
            else:
                k = heappop(que)
                C[k] = 0
                s[k] = 0
                s[q-1] = 1
                heappush(que, q-1)
                write("%d\n" % (k+1))
                update(k, q-1, 2)
        else:
            v = query(q-1)
            if v == q-1:
                write("%d\n" % q)
            else:
                s[v] = 1
                s[q-1] = 0
                if C[v] == 0:
                    heappush(que, v)
                    C[v] = 1
                write("%d\n" % (v + 1))
                update(v, q-1, -2)
solve()
