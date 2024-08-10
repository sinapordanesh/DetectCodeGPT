def OneStrokePath():
    from collections import deque
    import copy
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    ans = 0
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    q = deque()
    q.append([0, []])
        
    while q:
        x0, route0 = q.pop()
        if x0 in route0:
            continue
        route1 = copy.deepcopy(route0)
        route1.append(x0)
        if len(route1) == n:
            ans += 1
        for i in graph[x0]:
            if i in route1:
                continue
            q.append([i, route1])
    print(ans)  

if __name__ == '__main__':
    OneStrokePath()
    
