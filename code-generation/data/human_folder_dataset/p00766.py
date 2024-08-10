from collections import deque


class Dinic:
    """
    Dinicのアルゴリズム。最大流問題を解くことができます。
    https://tjkendev.github.io/procon-library/python/max_flow/dinic.html
    """

    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    def bfs(self, s, t):
        self.level = level = [None]*self.N
        deq = deque([s])
        level[s] = 0
        G = self.G
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in G[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        return level[t] is not None

    def dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        INF = 10**9 + 7
        G = self.G
        while self.bfs(s, t):
            *self.it, = map(iter, self.G)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow


def get_corner2corner_lines(B):
    H = len(B)
    W = len(B[0])
    vertical = []
    for i in range(H-1):
        for j in range(W-1):
            square = [B[i][j:j+2], B[i+1][j:j+2]]
            if square in [[".#", "##"], ["#.", "##"]]:
                tmp_i = i
                while tmp_i+1 < H and B[tmp_i+1][j:j+2] == "##":
                    tmp_i += 1
                if tmp_i+1 < H and B[tmp_i+1][j:j+2] in ["#.", ".#"]:
                    vertical.append((i, j, tmp_i))
    return vertical


def rotate(B):
    H = len(B)
    W = len(B[0])
    C = ["" for j in range(W)]
    for j in range(W):
        for i in range(H):
            C[j] += B[i][j]
    return C


def solve(B):
    H = len(B)
    W = len(B[0])

    horizontal = []
    vertical = []
    corners = 0
    for i in range(H-1):
        for j in range(W-1):
            square = [B[i][j:j+2], B[i+1][j:j+2]]
            if square[0].count("#")+square[1].count("#") == 3:
                corners += 1
    vertical = get_corner2corner_lines(B)
    horizontal = get_corner2corner_lines(rotate(B))

    H = len(horizontal)
    V = len(vertical)
    source = H+V
    sink = source+1
    n = H+V+2
    dinic = Dinic(n)
    for i in range(H):
        dinic.add_edge(source, i, 1)
    for i in range(V):
        dinic.add_edge(H+i, sink, 1)

    for i, (b, a, s) in enumerate(horizontal):
        for j, (c, d, t) in enumerate(vertical):
            if c <= a <= t and b <= d <= s:
                dinic.add_edge(i, H+j, 1)

    max_flow = dinic.flow(source, sink)
    ans = corners-(H+V-max_flow)+1
    return ans


def main():
    while True:
        H, W = map(int, input().split())
        if H == 0:
            break
        B = [input() for _ in range(H)]
        ans = solve(B)
        print(ans)


if __name__ == "__main__":
    main()

