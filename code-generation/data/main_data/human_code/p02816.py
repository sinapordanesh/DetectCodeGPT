from bisect import bisect_left
import sys
input = sys.stdin.readline

class Compress:

    def __init__(self, vs):
        self.xs = list(set(vs))
        self.xs.sort()

    def compress(self, x):
        return bisect_left(self.xs, x)

    def decompress(self, i):
        return self.xs[i]

def suffix_array(s):
    n = len(s)
    comp = Compress(s)
    t = [comp.compress(s[i]) for i in range(n)]
    cnt = [0] * n
    for i in range(n):
        cnt[t[i]] += 1
    for i in range(1, n):
        cnt[i] += cnt[i-1]
    p = [0] * n
    for i in range(n):
        cnt[t[i]] -= 1
        p[cnt[t[i]]] = i
    c = [0] * n
    cl = 0
    for i in range(1, n):
        if s[p[i]] != s[p[i-1]]:
            cl += 1
        c[p[i]] = cl

    pn = [0] * n
    cn = [0] * n
    h = 0
    while (1 << h) < n:
        for i in range(n):
            pn[i] = p[i] - (1 << h)
            if pn[i] < 0:
                pn[i] += n
        cnt = [0] * n
        for i in range(n):
            cnt[c[pn[i]]] += 1
        for i in range(1, n):
            cnt[i] += cnt[i-1]
        for i in range(n)[::-1]:
            cnt[c[pn[i]]] -= 1
            p[cnt[c[pn[i]]]] = pn[i]
        cn[p[0]] = 0
        cl = 0
        for i in range(1, n):
            cur = (c[p[i]], c[(p[i] + (1 << h)) % n])
            prev = (c[p[i-1]], c[(p[i-1] + (1 << h)) % n])
            if cur != prev:
                cl += 1
            cn[p[i]] = cl
        c, cn = cn, c
        h += 1
    return p


def bin_search(a, b, sa, lower):
    lb, ub = -1, N
    while ub - lb > 1:
        m = (lb + ub) // 2
        for i in range(N):
            j = (sa[m] + i) % N
            if a[i] < b[j]:
                ub = m
                break
            if a[i] > b[j]:
                lb = m
                break
        else:
            if lower:
                ub = m
            else:
                lb = m
    return ub

N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [a[i] ^ a[(i+1)%N] for i in range(N)]
d = [b[i] ^ b[(i+1)%N] for i in range(N)]
sa = suffix_array(d)
lb = bin_search(c, d, sa, True)
ub = bin_search(c, d, sa, False)
ans = []
for j in range(lb, ub):
    k = (N - sa[j]) % N
    x = a[k] ^ b[0]
    ans.append((k, x))
ans.sort()
for k, x in ans:
    print(k, x)