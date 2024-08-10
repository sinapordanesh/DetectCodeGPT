from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)

        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


while True:
    n, p1, p2 = (int(s) for s in input().split())
    if (n, p1, p2) == (0, 0, 0):
        break

    p = p1 + p2
    tree = UnionFind(p * 2)
    unions = defaultdict(list)

    for i in range(n):
        xs, ys, a = input().split()
        x, y = int(xs) - 1, int(ys) - 1
        if a == 'yes':
            tree.unite(x, y)
            tree.unite(x + p, y + p)
        else:
            tree.unite(x, y + p)
            tree.unite(x + p, y)

    for i in range(p):
        unions[tree.find(i)].append(i)
    roots = []
    sides = []
    diffs = []
    rest = p1
    for i in range(p):
        if i in unions:
            member_len, backside_len = len(unions[i]), len(unions[i + p])
            if member_len == backside_len:
                rest = -1
                break
            elif member_len < backside_len:
                diff = backside_len - member_len
                rest -= member_len
                sides.append(0)
            else:
                diff = member_len - backside_len
                sides.append(1)
                rest -= backside_len
            roots.append(i)
            diffs.append(diff)
    if rest < 0:
        print('no')
        continue

    dp = [[1] + [0] * rest for i in range(len(roots) + 1)]

    for i in reversed(range(len(roots))):
        for j in range(1, rest + 1):
            if j < diffs[i]:
                if dp[i + 1][j]:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0
            else:
                if dp[i + 1][j] and dp[i + 1][j - diffs[i]]:
                    dp[i][j] = 3
                elif dp[i + 1][j - diffs[i]]:
                    dp[i][j] = 2
                elif dp[i + 1][j]:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0

    divines = []
    for i in range(len(roots)):
        if dp[i][rest] == 1:
            divines.extend(unions[roots[i] + p * sides[i]])
        elif dp[i][rest] == 2:
            divines.extend(unions[roots[i] + p * (1 - sides[i])])
            rest -= diffs[i]
        else:
            print('no')
            break
    else:
        divines.sort()
        for divine in divines:
            print(divine + 1)
        print('end')