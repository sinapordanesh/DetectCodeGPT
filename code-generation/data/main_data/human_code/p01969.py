import re

def main():
    H, W, s, t = input().split()

    H, W = map(int, (H, W))
    s, t = map(lambda ch: ord(ch)-ord('A'), (s, t))

    a = [input() for i in range(H)]
    # b is transpose of a
    b = [''.join([a[i][j] for i in range(H)]) for j in range(W)]

    # Parse paths
    paths = []
    path_h_re = re.compile(r'o[A-Z]o(?:-+o[A-Z]o)+')
    path_v_re = re.compile(r'o[A-Z]o(?:\|+o[A-Z]o)+')
    for a_i in a: paths.extend(path_h_re.findall(a_i))
    for b_i in b: paths.extend(path_v_re.findall(b_i))
    paths = [re.sub(r'[^A-Z]+', '', e) for e in paths]

    # Make a graph
    INF = 50
    g = [[INF for j in range(26)] for i in range(26)]
    for path in paths:
        for u, v in zip(path[:-1], path[1:]):
            u = ord(u)-ord('A')
            v = ord(v)-ord('A')
            g[u][v] = g[v][u] = 1

    # Solve a shortest-path problem
    for k in range(26):
        g = [
            [min(g[i][j], g[i][k]+g[k][j]) for j in range(26)]
            for i in range(26)
        ]

    print(g[s][t])
    return 0

if __name__ == '__main__':
    exit(main())

