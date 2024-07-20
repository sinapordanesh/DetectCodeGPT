def range_sum_query(n, queries):
    arr = [0] * (n+1)
    result = []
    
    def add(i, x):
        arr[i] += x
    
    def getSum(s, t):
        result.append(sum(arr[s:t+1]))
    
    for query in queries:
        if query[0] == 0:
            add(query[1], query[2])
        elif query[0] == 1:
            getSum(query[1], query[2])
    
    return result

# Sample Input
n = 3
queries = [
    (0, 1, 1),
    (0, 2, 2),
    (0, 3, 3),
    (1, 1, 2),
    (1, 2, 2)
]

# Sample Output
print(range_sum_query(n, queries))