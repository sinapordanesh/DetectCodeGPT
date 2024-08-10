def process_queries(N, Q, A, queries):
    for query in queries:
        if query[0] == 1:
            A[query[1]-1] = query[2]
        elif query[0] == 2:
            print(max(A[query[1]-1:query[2]]))
        elif query[0] == 3:
            found = False
            for i in range(query[1]-1, N):
                if A[i] >= query[2]:
                    print(i+1)
                    found = True
                    break
            if not found:
                print(N+1)