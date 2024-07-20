def min_sum_of_salaries(N, contributions, M, relationships):
    graph = {}
    
    for i in range(1, N+1):
        graph[i] = []
    
    for a, b in relationships:
        graph[a].append(b)
    
    visited = [False] * (N+1)
    stack = []
    
    def topological_sort(node):
        visited[node] = True
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                topological_sort(neighbor)
        
        stack.append(node)
    
    for i in range(1, N+1):
        if not visited[i]:
            topological_sort(i)
    
    stack.reverse()
    
    dp = [0] * (N+1)
    
    for node in stack:
        for neighbor in graph[node]:
            dp[neighbor] = max(dp[neighbor], dp[node] + 1)
    
    total_salary = sum(contributions)
    
    for i in range(1, N+1):
        total_salary += dp[i]
    
    return total_salary

# Sample Input
N = 3
contributions = [1, 3, 3]
M = 2
relationships = [(1, 2), (1, 3)]
print(min_sum_of_salaries(N, contributions, M, relationships))

N = 3
contributions = [1, 2, 3]
M = 2
relationships = [(1, 2), (1, 3)]
print(min_sum_of_salaries(N, contributions, M, relationships))

N = 4
contributions = [1, 1, 2, 2]
M = 2
relationships = [(1, 2), (3, 4)]
print(min_sum_of_salaries(N, contributions, M, relationships))

N = 5
contributions = [1, 2, 5, 5, 1]
M = 6
relationships = [(1, 2), (4, 1), (2, 3), (5, 2), (4, 3), (4, 5)]
print(min_sum_of_salaries(N, contributions, M, relationships))

N = 6
contributions = [4, 3, 2, 1, 5, 3]
M = 7
relationships = [(4, 2), (1, 5), (2, 6), (6, 5), (4, 1), (1, 6), (6, 3)]
print(min_sum_of_salaries(N, contributions, M, relationships))