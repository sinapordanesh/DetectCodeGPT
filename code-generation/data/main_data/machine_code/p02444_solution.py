def rotate_elements(n, A, q, queries):
    for query in queries:
        b, m, e = query
        for k in range(e - b):
            temp = A[b + k]
            A[b + k] = A[b + (k + (e - m)) % (e - b)]
            A[b + (k + (e - m)) % (e - b)] = temp
    return A

n = 11
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
q = 1
queries = [[2, 6, 9]]

result = rotate_elements(n, A, q, queries)
print(' '.join(map(str, result)))