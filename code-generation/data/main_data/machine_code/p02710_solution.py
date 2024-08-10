def solve_tree_color_paths():
    from collections import defaultdict

    def dfs(node, parent, color):
        nonlocal result
        for nei in graph[node]:
            if nei == parent:
                continue
            result[color].append(color_count[colors[nei]])
            for k in range(1, N+1):
                color_count[k] += 1 if colors[nei] == k else 0
            dfs(nei, node, colors[nei])
            for k in range(1, N+1):
                color_count[k] -= 1 if colors[nei] == k else 0
       
    N = int(input())
    colors = list(map(int, input().split()))
    graph = defaultdict(list)
    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    result = defaultdict(list)
    color_count = [0] * (N+1)
    dfs(1, 0, colors[1])
    for i in range(1, N+1):
        print(sum(result[i]))  

solve_tree_color_paths()