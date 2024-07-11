from string import ascii_uppercase
import sys
readline = sys.stdin.readline
write = sys.stdout.write

conv = ascii_uppercase.find

def solve():
    N = int(readline())
    if N == 0:
        return False
    W = [tuple(map(conv, readline().strip())) for i in range(N)]
    S = []
    T = set()
    for s in readline().strip()[:-1].split():
        e = tuple(map(conv, s))
        S.append(e)
        T.add(e)
    *T, = T
    U = []
    for s in T:
        g = []
        for i, w in enumerate(W):
            if len(w) != len(s):
                continue
            p = [-1]*26
            l = len(w)
            for k in range(l):
                if p[s[k]] == p[w[k]] == -1:
                    p[s[k]] = w[k]
                    p[w[k]] = s[k]
                elif p[s[k]] == -1 or p[w[k]] == -1 or p[s[k]] != w[k]:
                    break
            else:
                g.append(i)
        U.append((s, g))
    L = len(U)
    U.sort(key = lambda x: len(x[1]))
    res = None
    cnt = 0
    def dfs(i, p0, used):
        nonlocal res, cnt
        if i == L:
            res = p0[:]
            cnt += 1
            return
        p = [0]*26
        s, g = U[i]
        for j in g:
            if used[j]:
                continue
            w = W[j]
            p[:] = p0

            l = len(w)
            for k in range(l):
                if p[s[k]] == p[w[k]] == -1:
                    p[s[k]] = w[k]
                    p[w[k]] = s[k]
                elif p[s[k]] == -1 or p[w[k]] == -1 or p[s[k]] != w[k]:
                    break
            else:
                used[j] = 1
                dfs(i+1, p, used)
                used[j] = 0
            if cnt >= 2:
                return
    dfs(0, [-1]*26, [0]*N)
    if cnt != 1:
        write("-.\n")
    else:
        cA = ord("A")
        ans = []
        for s in S:
            t = []
            for e in s:
                t.append(chr(res[e] + cA))
            ans.append("".join(t))
        write(" ".join(ans))
        write(".\n")
    return True
while solve():
    ...
