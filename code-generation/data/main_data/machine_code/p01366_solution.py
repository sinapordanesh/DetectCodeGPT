def road_construction():
    while True:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            break
        
        edges = []
        for _ in range(M):
            u, v, d, c = map(int, input().split())
            edges.append((u, v, d, c))
        
        costs = [float('inf')] * N
        costs[0] = 0
        
        for _ in range(N-1):
            for u, v, d, c in edges:
                if costs[u-1] != float('inf') and costs[u-1] + c < costs[v-1]:
                    costs[v-1] = costs[u-1] + c
        
        total_cost = sum([c for _, _, _, c in edges])
        min_cost = min(costs)
        
        print(total_cost - min_cost)

road_construction()