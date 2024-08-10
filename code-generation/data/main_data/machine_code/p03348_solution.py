import sys

def good_coloring_of_vertices(N, edges):
    adj_list = {}
    for i in range(1, N+1):
        adj_list[i] = []
    
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])
    
    colorfulness = 0
    leaves = sys.maxsize
    
    for i in range(1, N+1):
        leaf_count = sum(1 for v in adj_list[i] if len(adj_list[v]) == 1)
        if leaf_count < leaves:
            leaves = leaf_count
        colorfulness = max(colorfulness, len(adj_list[i]) - 1)
    
    print(colorfulness, leaves)

# Sample Input
N = 5
edges = [(1, 2), (2, 3), (3, 4), (3, 5)]
good_coloring_of_vertices(N, edges)