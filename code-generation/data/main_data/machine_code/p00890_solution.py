def test_case_tweaking(n, m, c, edges):
    min_changes = float('inf')
    for i in range(1, n+1):
        adj_list = {}
        for edge in edges:
            if edge[0] not in adj_list:
                adj_list[edge[0]] = []
            adj_list[edge[0]].append((edge[1], edge[2]))
        visited = [False] * (n+1)
        queue = [(1, 0)]
        while queue:
            node, cost = queue.pop(0)
            visited[node] = True
            if node == n:
                min_changes = min(min_changes, cost)
                break
            for neighbor, edge_cost in adj_list.get(node, []):
                if not visited[neighbor] and cost + edge_cost <= c:
                    queue.append((neighbor, cost + edge_cost))
    return min_changes

# Sample Input
print(test_case_tweaking(3, 3, 3, [(1, 2, 3), (2, 3, 3), (1, 3, 8)])) # Output: 1
print(test_case_tweaking(12, 12, 2010, [(1, 2, 0), (2, 3, 3000), (3, 4, 0), (4, 5, 3000), (5, 6, 3000), (6, 12, 2010)])) # Output: 2
print(test_case_tweaking(18, 1, 1, [(1, 2, 9), (1, 3, 2), (1, 4, 6), (2, 5, 0), (2, 6, 10), (2, 7, 2), (3, 5, 10), (3, 6, 3), (3, 7, 10), (4, 7, 6), (5, 8, 10), (6, 8, 2), (6, 9, 11), (7, 9, 3), (8, 9, 9), (8, 10, 8), (9, 10, 1), (8, 2, 1)])) # Output: 3