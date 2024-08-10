def check_consistency(N, M, info):
    def find_parent(x, parent):
        if parent[x] != x:
            parent[x] = find_parent(parent[x], parent)
        return parent[x]

    parent = [i for i in range(N+1)]
    rank = [0] * (N+1)

    def union(x, y):
        root_x = find_parent(x, parent)
        root_y = find_parent(y, parent)

        if root_x == root_y:
            return

        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y
            if rank[root_x] == rank[root_y]:
                rank[root_y] += 1

    for i in range(M):
        L, R, D = info[i]
        union(L, R)

    for i in range(1, N+1):
        find_parent(i, parent)

    for i in range(M):
        L, R, D = info[i]
        if parent[L] != parent[R]:
            if abs(parent[L] - parent[R]) != D:
                return "No"
    return "Yes"

N, M = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(M)]

print(check_consistency(N, M, info))