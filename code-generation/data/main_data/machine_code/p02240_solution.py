def connected_components(n, m, relations, q, queries):
    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def unite(x, y):
        x = find(x)
        y = find(y)
        if x != y:
            parent[x] = y

    parent = [i for i in range(n)]
    for s, t in relations:
        unite(s, t)

    result = []
    for s, t in queries:
        if find(s) == find(t):
            result.append("yes")
        else:
            result.append("no")

    return result

n, m = map(int, input().split())
relations = [tuple(map(int, input().split())) for _ in range(m)]
q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(q)]

for res in connected_components(n, m, relations, q, queries):
    print(res)