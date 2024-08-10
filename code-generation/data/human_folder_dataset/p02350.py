import sys
readline = sys.stdin.readline
write = sys.stdout.write

N, Q = map(int, input().split())
INF = 2**31-1

LV = (N-1).bit_length()
N0 = 2**LV
data = [INF]*(2*N0)
lazy = [None]*(2*N0)

def gindex(l, r):
    L = l + N0; R = r + N0
    lm = (L // (L & -L)) >> 1
    rm = (R // (R & -R)) >> 1
    while L < R:
        if R <= rm:
            yield R
        if L <= lm:
            yield L
        L >>= 1; R >>= 1
    while L:
        yield L
        L >>= 1

def propagates(*ids):
    for i in reversed(ids):
        v = lazy[i-1]
        if v is None:
            continue
        lazy[2*i-1] = data[2*i-1] = lazy[2*i] = data[2*i] = v
        lazy[i-1] = None

def update(l, r, x):
    *ids, = gindex(l, r)
    propagates(*ids)

    L = N0 + l; R = N0 + r
    while L < R:
        if R & 1:
            R -= 1
            lazy[R-1] = data[R-1] = x
        if L & 1:
            lazy[L-1] = data[L-1] = x
            L += 1
        L >>= 1; R >>= 1
    for i in ids:
        data[i-1] = min(data[2*i-1], data[2*i])

def query(l, r):
    propagates(*gindex(l, r))
    L = N0 + l; R = N0 + r

    s = INF
    while L < R:
        if R & 1:
            R -= 1
            s = min(s, data[R-1])
        if L & 1:
            s = min(s, data[L-1])
            L += 1
        L >>= 1; R >>= 1
    return s


ans = []
for q in range(Q):
    t, *cmd = map(int, readline().split())
    if t:
        s, t = cmd
        ans.append(str(query(s, t+1)))
    else:
        s, t, x = cmd
        update(s, t+1, x)

write("\n".join(ans))
write("\n")
