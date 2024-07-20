def process_queries(N, Q, A, B, queries):
    time = 0
    for query in queries:
        time += min(abs(A - query), abs(B - query))
        if abs(A - query) < abs(B - query):
            A = query
        else:
            B = query
    return time
          
N, Q, A, B = map(int, input().split())
queries = list(map(int, input().split()))

print(process_queries(N, Q, A, B, queries))