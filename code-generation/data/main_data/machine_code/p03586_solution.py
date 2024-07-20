def process_queries(Q, queries):
    for i in range(Q):
        A, M = queries[i]
        for K in range(1, 2 * 10 ** 18 + 1):
            if A ** K % M == K:
                print(K)
                break
        else:
            print(-1)