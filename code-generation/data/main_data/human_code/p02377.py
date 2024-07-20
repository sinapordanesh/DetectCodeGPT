INF = float('inf')


def trace_back(sink, predecessors):
    p = predecessors[sink]
    while p is not None:
        v, i = p
        yield edges[v][i]
        p = predecessors[v]


def min_cost_flow(source, sink, required_flow):
    res = 0
    while required_flow:
        dist = [INF] * n
        dist[source] = 0
        predecessors = [None] * n

        while True:
            updated = False
            for v in range(n):
                if dist[v] == INF:
                    continue
                for i, (remain, target, cost, _) in enumerate(edges[v]):
                    new_dist = dist[v] + cost
                    if remain and dist[target] > new_dist:
                        dist[target] = new_dist
                        predecessors[target] = (v, i)
                        updated = True
            if not updated:
                break

        if dist[sink] == INF:
            return -1

        aug = min(required_flow, min(e[0] for e in trace_back(sink, predecessors)))
        required_flow -= aug
        res += aug * dist[sink]
        for e in trace_back(sink, predecessors):
            remain, target, cost, idx = e
            e[0] -= aug
            edges[target][idx][0] += aug
    return res


n, m, f = map(int, input().split())
edges = [[] for _ in range(n)]

for _ in range(m):
    s, t, c, d = map(int, input().split())
    es, et = edges[s], edges[t]
    ls, lt = len(es), len(et)
    es.append([c, t, d, lt])
    et.append([0, s, -d, ls])

print(min_cost_flow(0, n - 1, f))