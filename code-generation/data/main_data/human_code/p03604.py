import sys
input = sys.stdin.readline

MOD = 10**9 + 7

N = int(input())
ball = (tuple(int(x) for x in row.split()) for row in sys.stdin.readlines())

# x座標を1,2,...,N
# y座標をN+1,N+2,...,N+N

graph = [set() for _ in range(N+N+1)]
for x,y in ball:
    graph[x].add(y+N)
    graph[y+N].add(x)

visited = [False] * (N+N+1)
components = []
for x in range(1,N+N+1):
    if visited[x]:
        continue
    V = set([x])
    E = []
    q = [x]
    visited[x] = True
    while q:
        y = q.pop()
        for z in graph[y]:
            if y < z:
                E.append((y,z))
            if visited[z]:
                continue
            V.add(z)
            visited[z] = True
            q.append(z)
    components.append((V,E))

def make_get_pattern(V):
    deg1 = [x for x in V if len(graph[x]) == 1]
    get = {}
    while deg1:
        x = deg1.pop()
        if not graph[x]:
            continue
        y = graph[x].pop()
        se = graph[y]; se.remove(x)
        if len(se) == 1: deg1.append(y)
        if x < y:
            get[(x,y)] = 0
        else:
            get[(y,x)] = 1
    for x in V:
        if graph[x]:
            y = graph[x].pop()
            break
    # 残りはサイクル
    graph[y].remove(x)
    if x > y: x,y = y,x
    get[(x,y)] = 2
    while graph[x]:
        y = graph[x].pop()
        graph[y].remove(x)
        if x < y:
            get[(x,y)] = 3
        else:
            get[(y,x)] = 2
        x = y
    return get

def F(V,E):
    # V is connected
    if len(E) != len(V):
        return 0
    ret = 0
    E.sort()
    get = make_get_pattern(V)
    den1,den2 = 1,1
    dp1 = {x:0 for x in V}
    dp2 = {x:0 for x in V}
    for x,y in E:
        if get[(x,y)] == 0:
            k1 = dp1[x] + 1; k2 = dp2[x] + 1
        elif get[(x,y)] == 1:
            k1 = dp1[y] + 1; k2 = dp2[y] + 1
        elif get[(x,y)] == 2:
            k1 = dp1[x] + 1; k2 = dp2[y] + 1
        else:
            k1 = dp1[y] + 1; k2 = dp2[x] + 1
        dp1[x] += k1; dp1[y] += k1
        dp2[x] += k2; dp2[y] += k2
        den1 *= k1; den2 *= k2
        den1 %= MOD; den2 %= MOD
    return sum(pow(x,MOD-2,MOD) for x in (den1,den2))

prob = 1
for c in components:
    prob *= F(*c)
    prob %= MOD

answer = prob
for n in range(1,N+N+1):
    answer *= n
    answer %= MOD
print(answer)