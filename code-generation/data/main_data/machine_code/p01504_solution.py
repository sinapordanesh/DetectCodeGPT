def min_destroying_cost():
    case = 1
    while True:
        n, t, k = map(int, input().split())
        if n == 0 and t == 0 and k == 0:
            break
        edges = []
        for _ in range(n-1):
            edge = list(map(int, input().split()))
            edges.append(edge)
        bases = set()
        for _ in range(t):
            base = int(input())
            bases.add(base)
        adj_list = {i: [] for i in range(1, n+1)}
        for edge in edges:
            adj_list[edge[0]].append((edge[1], edge[2]))
            adj_list[edge[1]].append((edge[0], edge[2]))
        
        def dfs(node, parent):
            num_bases = 1 if node in bases else 0
            total_cost = 0
            for neighbor, cost in adj_list[node]:
                if neighbor != parent:
                    child_bases, child_cost = dfs(neighbor, node)
                    num_bases += child_bases
                    total_cost += min(child_cost, cost)
            return num_bases, total_cost
        
        result = dfs(1, -1)
        print(f"Case {case}: {result[1]}")
        case += 1

min_destroying_cost()