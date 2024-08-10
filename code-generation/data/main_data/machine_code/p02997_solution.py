def construct_graph(N, K):
    if K > (N*(N-1)) // 2:
        print(-1)
    else:
        print(N)
        edges = []
        count = 0
        for i in range(1, N):
            for j in range(i+1, N+1):
                edges.append((i, j))
                count += 1
                if count == K:
                    break
            if count == K:
                break
        for edge in edges:
            print(edge[0], edge[1])