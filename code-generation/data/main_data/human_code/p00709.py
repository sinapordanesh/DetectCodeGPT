import sys
readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    W, H = map(int, readline().split())
    if W == 0:
        return False
    MP = [list(map(int, input().split())) for i in range(H)]
    C = [[0]*W for i in range(H)]
    for j in range(W):
        cur = 0
        for i in range(H-1, -1, -1):
            if MP[i][j]:
                cur += 1
            else:
                cur = 0
            C[i][j] = cur
    D = [[0]*W for i in range(H)]
    E = [[0]*W for i in range(H)]
    for i in range(H):
        st = []
        for j in range(W):
            c = C[i][j]
            last = j
            while st and c <= st[-1][0]:
                p, k = st.pop()
                last = k
                d = min(j - k, p)
                for e in range(k, j-d+1):
                    D[i][e] = max(D[i][e], d)
            st.append((c, last))
        while st:
            p, k = st.pop()
            d = min(W - k, p)
            if d:
                for e in range(k, W-d+1):
                    D[i][e] = max(D[i][e], d)
        st.append((W, 0))

    S = []
    Z = [0]*(W*H)
    ALL = 0
    for i in range(H):
        for j in range(W):
            if MP[i][j]:
                ALL |= 1 << (i*W + j)
            if E[i][j] < D[i][j]:
                S.append(i*W + j)
                Z[i*W + j] = D[i][j]
            E[i][j] = e = max(E[i][j], D[i][j])
            if e > 1:
                E[i+1][j] = max(E[i+1][j], e-1)
                E[i][j+1] = max(E[i][j+1], e-1)
                E[i+e-1][j+e-1] = max(E[i+e-1][j+e-1], 1)

    SN = len(S)
    L = max(W, H)
    T = [0]*(L+1)
    for d in range(1, L+1):
        v = 0
        for i in range(d):
            for j in range(d):
                v |= 1 << (i*W + j)
        T[d] = v
    BS = [0]*SN; CS = [0]*SN
    for i in range(SN):
        s = S[i]
        BS[i] = T[Z[s]] << s
        CS[i] = 1 << s

    memo = [{} for i in range(SN)]
    def dfs(i, state):
        if i == SN:
            if state == ALL:
                return 0
            return W*H
        if state in memo[i]:
            return memo[i][state]
        r = W*H
        if state & CS[i]:
            r = min(r, dfs(i+1, state))
        if state & BS[i] != BS[i]:
            r = min(r, dfs(i+1, state | BS[i]) + 1)
        memo[i][state] = r
        return r
    write("%d\n" % dfs(0, 0))
    return True
while solve():
    ...
