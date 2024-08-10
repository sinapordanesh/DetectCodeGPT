class Cube:
    def __init__(self, x, y, z, s):
        self.x, self.y, self.z = x, y, z
        self.s = s

    def is_in_cube(self, x, y, z):
        return self.x <= x <= self.x + self.s and self.y <= y <= self.y + self.s and self.z <= z <= self.z + self.s

    def intersect(self, C):
        dxyz = [(0, 0, 0),
                (C.s, 0, 0), (0, C.s, 0), (0, 0, C.s),
                (C.s, C.s, 0), (C.s, 0, C.s), (0, C.s, C.s),
                (C.s, C.s, C.s)]
        for dx1, dy1, dz1 in dxyz:
            nx1, ny1, nz1 = C.x + dx1, C.y + dy1, C.z + dz1
            if self.is_in_cube(nx1, ny1, nz1):
                for dx2, dy2, dz2 in dxyz:
                    nx2, ny2, nz2 = self.x + dx2, self.y + dy2, self.z + dz2
                    if C.is_in_cube(nx2, ny2, nz2):
                        a, b, c = abs(nx1 - nx2), abs(ny1 - ny2), abs(nz1 - nz2)
                        if a * b * c == 0:
                            continue
                        # print(a, b, c, end=':')
                        return 2 * (a * b + b * c + c * a)
        return 0


edges = list()
inters = dict()


def calc_overlap(vs):
    ret = sum(inters.get((vs[i], vs[i + 1]), 0) for i in range(len(vs) - 1))
    if len(vs) > 2:
        ret += inters.get((vs[-1], vs[0]), 0)
    return ret


def dfs(v, par, vs, res):
    if res == 0:
        return calc_overlap(vs)

    ret = -1

    for e in edges[v]:
        if e != par:
            vs.append(e)
            ret = max(ret, dfs(e, v, vs, res - 1))
            vs.pop()
    return ret


INF = 10 ** 9
while True:
    N, K, S = map(int, input().split())
    # print((N, K, S))
    if not (N | K | S):
        break
    cubes = []
    for _ in range(N):
        x, y, z = map(int, input().split())
        cubes.append(Cube(x, y, z, S))
    # cubes = [Cube(*map(int, input().split()), S) for _ in range(N)]
    edges = [[] for _ in range(N)]
    inters = dict()
    for i in range(N):
        for j in range(i + 1, N):
            sur = cubes[i].intersect(cubes[j])
            if sur > 0:
                # print(i, j, cubes[i].intersect(cubes[j]))
                inters[i, j] = inters[j, i] = sur
                edges[i].append(j)
                edges[j].append(i)
    # print(edges, inters)

    ans = -1
    for i in range(N):
        ans = max(ans, dfs(i, -1, [i], K - 1))

    print(-1 if ans == -1 else S * S * 6 * K - ans)