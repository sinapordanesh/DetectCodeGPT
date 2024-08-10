def min_roads_same_state(N, M, roads):
    adj_list = [[] for _ in range(N)]
    for road in roads:
        a, b = road
        adj_list[a-1].append(b-1)
        adj_list[b-1].append(a-1)
    
    for i in range(N):
        taka = [i]
        hashi = []
        visited = [False] * N
        visited[i] = True
        stack = [i]
        
        while stack:
            node = stack.pop()
            for neighbor in adj_list[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    if neighbor not in taka:
                        taka.append(neighbor)
                        stack.append(neighbor)
                    else:
                        hashi.append(neighbor)
        
        for node in taka:
            for neighbor in adj_list[node]:
                if neighbor in taka:
                    break
            else:
                break
        else:
            return M - len(taka) * (len(taka) - 1) // 2
        
    return -1

# Sample Input 4
print(min_roads_same_state(10, 39, [(7, 2), (7, 1), (5, 6), (5, 8), (9, 10), (2, 8), (8, 7), (3, 10), (10, 1), (8, 10), (2, 3), (7, 4), (3, 9), (4, 10), (3, 4), (6, 1), (6, 7), (9, 5), (9, 7), (6, 9), (9, 4), (4, 6), (7, 5), (8, 3), (2, 5), (9, 2), (10, 7), (8, 6), (8, 9), (7, 3), (5, 3), (4, 5), (6, 3), (2, 10), (5, 10), (4, 2), (6, 2), (8, 4), (10, 6)]))