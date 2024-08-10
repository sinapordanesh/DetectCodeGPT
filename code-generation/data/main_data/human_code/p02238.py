# -*- coding: utf-8 -*-


class Graph:
    def __init__(self, n, adj_matrix):
        self.n = n
        self.adj_matrix = adj_matrix

    def show(self):
        for _ in self.adj_matrix:
            print(*_)

    def dfs(self):
        self.states = [2] * self.n
        self.d = [None] * self.n
        self.f = [None] * self.n
        self.time = 0

        for u in range(self.n):
            if self.states[u] == 2:
                self.dfs_visit(u)

    def dfs_visit(self, u):
        self.states[u] = 1
        self.time += 1
        self.d[u] = self.time

        for v, edge in enumerate(self.adj_matrix[u]):
            if edge and self.states[v] == 2:
                self.dfs_visit(v)

        self.states[u] = 0
        self.time += 1
        self.f[u] = self.time

    def show_dfs(self, start=0):
        self.dfs()
        for i, (d, f) in enumerate(zip(self.d, self.f)):
            print(i + 1, d, f)


if __name__ == '__main__':
    n = int(input())
    adj_matrix = [[0] * n for i in range(n)]
    for i in range(n):
        for v in input().split()[2:]:
            adj_matrix[i][int(v) - 1] = 1

    g = Graph(n, adj_matrix)
    g.show_dfs()

