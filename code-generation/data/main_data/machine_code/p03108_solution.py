def find_inconvenience(N, M, bridges):
    def find_root(parent, i):
        if parent[i] == i:
            return i
        return find_root(parent, parent[i])
    
    def union(parent, rank, x, y):
        x_root = find_root(parent, x)
        y_root = find_root(parent, y)
        
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1
    
    inconveniences = [0] * M
    parent = [i for i in range(N + 1)]
    rank = [0] * (N + 1)
    
    for i in range(M):
        a, b = bridges[i]
        a_root = find_root(parent, a)
        b_root = find_root(parent, b)
        
        if a_root != b_root:
            inconveniences[i] = inconveniences[i - 1] + rank[a_root] * rank[b_root] * 2
            union(parent, rank, a_root, b_root)
        else:
            inconveniences[i] = inconveniences[i - 1]
    
    return inconveniences

# Sample Input 1
N = 4
M = 5
bridges = [(1, 2), (3, 4), (1, 3), (2, 3), (1, 4)]
print(find_inconvenience(N, M, bridges))

# Sample Input 2
N = 6
M = 5
bridges = [(2, 3), (1, 2), (5, 6), (3, 4), (4, 5)]
print(find_inconvenience(N, M, bridges))

# Sample Input 3
N = 2
M = 1
bridges = [(1, 2)]
print(find_inconvenience(N, M, bridges))