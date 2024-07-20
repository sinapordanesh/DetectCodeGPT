def process_queries(N, Q, arr, queries):
    for query in queries:
        if query[0] == 0:
            arr[query[1]] += query[2]
        elif query[0] == 1:
            print(sum(arr[query[1]:query[2]])) 

# Sample Input
N, Q = 5, 5
arr = [1, 2, 3, 4, 5]
queries = [
    [1, 0, 5],
    [1, 2, 4],
    [0, 3, 10],
    [1, 0, 5],
    [1, 0, 3]
]

process_queries(N, Q, arr, queries)