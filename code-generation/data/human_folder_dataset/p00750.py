def bellman_ford(graph, source):
    d = [INF] * n
    d[g] = ''

    for i in range(n * 6 + 1):
        update = False
        for e in graph:
            if d[e[1]] != INF and d[e[0]] > e[2] + d[e[1]]:
                d[e[0]] = e[2] + d[e[1]]
                update = True
        if len(d[s]) > n * 6:
            return None
        if not update:
            return d[s]
    else:
        return d[s]


INF = '{'
while True:
    n, a, s, g = (int(s) for s in input().split())
    if (n, a, s, g) == (0, 0, 0, 0):
        break

    flag = []
    edge = []
    es = []
    for i in range(a):
        xs, ys, labi = input().split()
        es.append((int(xs), int(ys), labi))

    spell = bellman_ford(es, g)
    if spell == INF or spell is None:
        print('NO')
    else:
        print(spell)