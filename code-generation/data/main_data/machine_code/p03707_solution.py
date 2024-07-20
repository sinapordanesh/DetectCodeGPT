def connected_components(N, M, Q, grid, queries):
    def dfs(i, j):
        if i < 0 or i >= N or j < 0 or j >= M or grid[i][j] == 0:
            return
        grid[i][j] = 0
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    
    def count_components():
        components = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    components += 1
                    dfs(i, j)
        return components
    
    result = []
    for query in queries:
        x1, y1, x2, y2 = query
        region = [row[y1-1:y2] for row in grid[x1-1:x2]]
        result.append(count_components())
    
    return result

# Sample Input 1
print(connected_components(3, 4, 4, [[1,1,0,1],[0,1,1,0],[1,1,0,1]], [[1,1,3,4],[1,1,3,1],[2,2,3,4],[1,2,2,4]]))

# Sample Input 2
print(connected_components(5, 5, 6, [[1,1,0,1,0],[0,1,1,1,0],[1,0,1,0,1],[1,1,1,0,1],[0,1,0,1,0]], [[1,1,5,5],[1,2,4,5],[2,3,3,4],[3,3,3,3],[3,1,3,5],[1,1,3,4]]))