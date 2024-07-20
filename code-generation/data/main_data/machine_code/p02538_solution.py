def replace_characters(N, Q, queries):
    S = ['1'] * N
    for query in queries:
        L, R, D = query
        for i in range(L-1, R):
            S[i] = D
        result = int("".join(S)) % 998244353
        print(result)

N, Q = 8, 5
queries = [(3, 6, 2), (1, 4, 7), (3, 8, 3), (2, 2, 2), (4, 5, 1)]
replace_characters(N, Q, queries)