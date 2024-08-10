def range_minimum_query(n, q, queries):
    arr = [2**31-1] * n

    def update(i, x):
        arr[i] = x

    def find(s, t):
        return min(arr[s:t+1])

    res = []
    for query in queries:
        if query[0] == 0:
            update(query[1], query[2])
        else:
            res.append(find(query[1], query[2]))
    
    return res

# Sample Input 1
n1 = 3
q1 = 5
queries1 = [[0, 0, 1], [0, 1, 2], [0, 2, 3], [1, 0, 2], [1, 1, 2]]
print(range_minimum_query(n1, q1, queries1))

# Sample Input 2
n2 = 1
q2 = 3
queries2 = [[1, 0, 0], [0, 0, 5], [1, 0, 0]]
print(range_minimum_query(n2, q2, queries2))