def process_queries(N, Q, A, queries):
    def count_inversions(arr):
        count = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] > arr[j]:
                    count += 1
        return count

    result = []
    for query in queries:
        if query[0] == 1:
            for i in range(query[1]-1, query[2]):
                A[i] = 1 - A[i]
        elif query[0] == 2:
            result.append(count_inversions(A[query[1]-1:query[2]]))
    
    return result

# Sample Input
N = 5
Q = 5
A = [0, 1, 0, 0, 1]
queries = [(2, 1, 5), (1, 3, 4), (2, 2, 5), (1, 1, 3), (2, 1, 2)]

print(*process_queries(N, Q, A, queries))