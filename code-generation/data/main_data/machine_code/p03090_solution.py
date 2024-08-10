def build_graph(N):
    if N % 2 == 0:
        S = N
    else:
        S = N + 1
    
    M = N - 1
    edges = []
    for i in range(1, N):
        edges.append((i, N))
    
    return M, edges

N = int(input())
M, edges = build_graph(N)
print(M)
for edge in edges:
    print(edge[0], edge[1])