n, m = map(int, input().split())
INF = 10**9
import sys
sys.setrecursionlimit(6000)
G = [[] for _ in range(n*m+2)]

def add_edge(s, t, cap):
    G[s].append([t, cap, len(G[t])])
    G[t].append([s, 0, len(G[s])-1])

def get_edges(s):
    pass

def dfs(v, t, f, used):
    """ 増加パスをDFSで探す、再帰バージョン
    Args:
        v (int): 探索の開始地点
        t (int): 探索の終了地点
        f (int): 流す量
        used (list): 訪れた点の記録
    Returns:
        int: 流すことのできた量
    """
    if v == t:
        return f
    used[v] = 1
    for idx, (nn, cap, rev) in enumerate(G[v]):
        if used[nn] == 0 and cap > 0:
            d = dfs(nn, t, min(f, cap), used)
            if d > 0:
                G[v][idx][1] -= d
                G[nn][rev][1] += d
                return d
    else:
        return 0

def flow(s, t):
    ans = 0
    while True:
        used = [0] * (n*m+2)
        f = dfs(s, t, INF, used)
        if f == 0:
            return ans
        ans += f


S = [list(input()) for _ in range(n)]

# n*mを始点, n*m+1を終点とする
for i, line in enumerate(S):
    for j, s in enumerate(line):
        cp = i*m+j
        if (i%2 == 0 and j%2 == 0) or (i%2 == 1 and j%2 == 1):
            if s == '.':
                add_edge(n*m, cp, 1)
                for mi, mj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    ni, nj = i+mi, j+mj
                    if 0 <= ni < n and 0 <= nj < m and S[ni][nj] == '.':
                        ep = ni*m+nj
                        add_edge(cp, ep, 1)
        else:
            if s == '.':
                add_edge(cp, n*m+1, 1)

f = flow(n*m, n*m+1)
print(f)

for a, cap, rev in G[n*m]:
    if cap == 0:
        for b, cap, rev in G[a]:
            if cap == 0:
                # a to b
                i, j = divmod(a, m)
                ii, jj = divmod(b, m)
                np = ii - i, jj - j
                if np == (1, 0):
                    S[i][j] = 'v'
                    S[ii][jj] = '^'
                elif np == (-1, 0):
                    S[i][j] = '^'
                    S[ii][jj] = 'v'
                elif np == (0, 1):
                    S[i][j] = '>'
                    S[ii][jj] = '<'
                elif np == (0, -1):
                    S[i][j] = '<'
                    S[ii][jj] = '>'
                break

for line in S:
    print(''.join(line))
