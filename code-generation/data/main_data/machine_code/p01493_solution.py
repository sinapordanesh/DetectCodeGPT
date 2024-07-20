def DisconnectedGame(V, matrix):
    def dfs(node, visited):
        visited[node] = 1
        for i in range(V):
            if matrix[node][i] == 'Y' and not visited[i]:
                dfs(i, visited)

    visited = [0] * V

    num_components = 0
    for i in range(V):
        if not visited[i]:
            num_components += 1
            dfs(i, visited)

    if num_components % 2 == 0:
        return "Hanako"
    else:
        return "Taro"